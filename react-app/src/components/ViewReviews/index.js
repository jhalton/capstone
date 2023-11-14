import "./ViewReviews.css";
import React from "react";
import { useModal } from "../../context/Modal";
import EditReviewModal from "../EditReviewModal";

const ViewReviews = ({ book, reviews, user }) => {
  const { setModalContent } = useModal();
  return (
    <div className="book-detail-reviews--container">
      <h1>View Reviews</h1>
      <div className="book-detail-reviews--reviews">
        {reviews.map((review) => (
          <li key={review.id}>
            <span className="book-detail-reviews--review-li">
              {review.rating}
              {review.userId === user.id ? (
                <span>
                  <i
                    class="fa-regular fa-pen-to-square"
                    onClick={() =>
                      setModalContent(
                        <EditReviewModal
                          bookId={book.id}
                          reviewDetails={review}
                        />
                      )
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
