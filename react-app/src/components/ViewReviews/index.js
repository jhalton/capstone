import "./ViewReviews.css";
import React from "react";
import { useModal } from "../../context/Modal";
import EditReviewModal from "../EditReviewModal";
import DeleteReviewModal from "../DeleteReviewModal";

const ViewReviews = ({ book, reviews, user }) => {
  const { setModalContent } = useModal();
  return (
    <div className="book-detail-reviews--container">
      <h1>View Reviews</h1>
      <div className="book-detail-reviews--reviews">
        {reviews
          .sort((a, b) => b.id - a.id)
          .map((review) => (
            <li key={review?.id}>
              <span
                className={
                  !review.spoiler
                    ? "book-detail-reviews--review-li"
                    : "book-detail-reviews--review-li spoiler"
                }
              >
                <span className="book-detail-reviews--rating">
                  {review.rating}
                  <i className="fa-solid fa-star"></i>
                </span>
                <span className="book-detail-reviews--penName">
                  {review.penName ? review.penName : "Anonymous"}
                </span>
                <span
                  className={
                    review.spoiler
                      ? "book-detail-reviews--review-spoiler"
                      : "book-detail-reviews--review"
                  }
                >
                  {review.review}
                </span>
                {review.spoiler ? (
                  <span className="book-detail-reviews--spoiler">
                    Spoiler?{" "}
                    <i className="fa-solid fa-check yes-spoiler-check"></i>
                  </span>
                ) : (
                  <span className="book-detail-reviews--spoiler">
                    Spoiler? <i className="fa-solid fa-x no-spoiler-x"></i>
                  </span>
                )}
                {review.userId === user?.id ? (
                  <span>
                    <i
                      className="fa-regular fa-pen-to-square"
                      onClick={() =>
                        setModalContent(
                          <EditReviewModal
                            bookId={book.id}
                            reviewDetails={review}
                            user={user}
                          />
                        )
                      }
                    ></i>
                    <i
                      className="fa-regular fa-trash-can"
                      onClick={() =>
                        setModalContent(<DeleteReviewModal review={review} />)
                      }
                    ></i>
                  </span>
                ) : null}
              </span>
            </li>
          ))}
      </div>
    </div>
  );
};

export default ViewReviews;
