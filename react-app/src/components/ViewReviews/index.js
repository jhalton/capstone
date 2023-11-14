import "./ViewReviews.css";
import React from "react";

const ViewReviews = ({ book, reviews }) => {
  return (
    <div className="book-detail-reviews--container">
      <h1>View Reviews</h1>
      <div className="book-detail-reviews--reviews">
        {reviews.map((review) => (
          <li key={review.id}>
            <span className="book-detail-reviews--review-li">
              {review.rating}
            </span>
          </li>
        ))}
      </div>
    </div>
  );
};

export default ViewReviews;
