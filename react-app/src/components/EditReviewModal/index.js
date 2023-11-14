import "./EditReviewModal.css";
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { editReview, getAllReviews } from "../../store/reviews";

const EditReviewModal = ({ bookId, reviewDetails }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const [pen_name, setPenName] = useState(reviewDetails.pen_name);
  const [review, setReview] = useState(reviewDetails.review);
  const [spoiler, setSpoiler] = useState(reviewDetails.spoiler);
  const [rating, setRating] = useState(reviewDetails.rating);
  const [errors, setErrors] = useState({});
  const reviewId = reviewDetails.id;

  const handleSubmit = async (e) => {
    e.preventDefault();

    const reviewData = {
      pen_name,
      rating,
      review,
      spoiler,
    };

    const data = await dispatch(editReview(reviewId, reviewData));
    if (data?.errors) {
      setErrors(data?.errors);
    } else {
      dispatch(getAllReviews(bookId)).then(closeModal());
    }
  };

  return (
    <div className="edit-review-modal--container">
      <form onSubmit={handleSubmit}>
        <label htmlFor="penName">Would you like to use a pen name?</label>
        <input
          id="penName"
          type="text"
          value={pen_name}
          onChange={(e) => setPenName(e.target.value)}
        />
        {errors.pen_name && <p className="errors">{errors.pen_name}</p>}
        <label htmlFor="review">How did you like the book?</label>
        <textarea
          id="review"
          value={review}
          onChange={(e) => setReview(e.target.value)}
        />
        {errors.review && <p className="errors">{errors.review}</p>}
        <label htmlFor="spoiler">Does your review contain spoilers?</label>
        <div>
          <label>
            Yes
            <input
              id="spoiler-yes"
              type="radio"
              value="true"
              name="spoiler"
              onChange={() => setSpoiler(true)}
            />
          </label>
          <label>
            No
            <input
              id="spoiler-no"
              type="radio"
              value="false"
              name="spoiler"
              onChange={() => setSpoiler(false)}
            />
          </label>
        </div>
        {errors.spoiler && <p className="errors">{errors.spoiler}</p>}
        <div className="edit-review-modal--stars">
          <div
            className={
              rating >= 1
                ? "edit-review-modal--rating-filled"
                : "edit-review-modal--rating-empty"
            }
          >
            <i
              className="fa-solid fa-star "
              onMouseEnter={() => setRating(1)}
            ></i>
          </div>
          <div
            className={
              rating >= 2
                ? "edit-review-modal--rating-filled"
                : "edit-review-modal--rating-empty"
            }
          >
            <i
              className="fa-solid fa-star "
              onMouseEnter={() => setRating(2)}
            ></i>
          </div>
          <div
            className={
              rating >= 3
                ? "edit-review-modal--rating-filled"
                : "edit-review-modal--rating-empty"
            }
          >
            <i
              className="fa-solid fa-star "
              onMouseEnter={() => setRating(3)}
            ></i>
          </div>
          <div
            className={
              rating >= 4
                ? "edit-review-modal--rating-filled"
                : "edit-review-modal--rating-empty"
            }
          >
            <i
              className="fa-solid fa-star "
              onMouseEnter={() => setRating(4)}
            ></i>
          </div>
          <div
            className={
              rating >= 5
                ? "edit-review-modal--rating-filled"
                : "edit-review-modal--rating-empty"
            }
          >
            <i
              className="fa-solid fa-star "
              onMouseEnter={() => setRating(5)}
            ></i>
          </div>
        </div>
        {errors.rating && <p className="errors">{errors.rating}</p>}
        <button type="submit">Save Changes</button>
      </form>
    </div>
  );
};

export default EditReviewModal;
