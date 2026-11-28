from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session, select, func
from models import Review, ReviewCreate, ReviewRead, ReviewUpdate
from db_config import get_session

router = APIRouter(prefix="/review", tags=["Review"])


@router.post("/", response_model=ReviewRead)
def create_review(review: ReviewCreate, session: Session = Depends(get_session)):
    db_review = Review(**review.model_dump())
    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review


@router.get("/", response_model=list[ReviewRead])
def list_reviews(
    play_name: str | None = Query(
        default=None, description="Filter reviews by play name"
    ),
    skip: int = Query(default=0, ge=0, description="Number of reviews to skip"),
    limit: int = Query(
        default=10, ge=1, le=50, description="Maximum number of reviews to return"
    ),
    session: Session = Depends(get_session),
):

    query = select(Review)
    if play_name:
        query = query.where(Review.play_name == play_name)
    query = query.offset(skip).limit(limit)
    reviews = session.exec(query).all()
    return reviews


@router.get("/average/{play_name}")
def get_average_rating(play_name: str, session: Session = Depends(get_session)):
    result = session.exec(
        select(func.avg(Review.rating), func.count(Review.id)).where(Review.play_name == play_name)  # type: ignore
    ).first()
    average_rating, review_count = result if result else (None, 0)

    if review_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No reviews found for play '{play_name}'",
        )

    return {
        "play_name": play_name,
        "average_rating": (
            round(average_rating, 2) if average_rating is not None else None
        ),
        "review_count": review_count,
    }


@router.get("/{review_id}", response_model=ReviewRead)
def get_review(review_id: int, session: Session = Depends(get_session)):
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Review with ID {review_id} not found",
        )
    return review


@router.patch("/{review_id}", response_model=ReviewRead)
def update_review(
    review_id: int, review_update: ReviewUpdate, session: Session = Depends(get_session)
):
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Review with ID {review_id} not found",
        )

    for key, value in review_update.model_dump(exclude_unset=True).items():
        setattr(review, key, value)

    session.add(review)
    session.commit()
    session.refresh(review)
    return review


@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(review_id: int, session: Session = Depends(get_session)):
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Review with ID {review_id} not found",
        )

    session.delete(review)
    session.commit()
    return None
