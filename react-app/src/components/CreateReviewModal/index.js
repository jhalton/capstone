import "./CreateReviewModal.css";
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { createReview, getAllReviews } from "../../store/reviews";
import { useModal } from "../../context/Modal";

const CreateReviewModal = ({ user, bookId }) => {
  const [pen_name, setPenName] = useState(user?.firstName || null);
  const [rating, setRating] = useState(null);
  const [review, setReview] = useState("");
  const [spoiler, setSpoiler] = useState(false);
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();
  const dispatch = useDispatch();
  console.log("CREATE REVIEW MODAL ERRORS", errors);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const reviewData = {
      pen_name,
      rating,
      review,
      spoiler,
    };

    const data = await dispatch(createReview(bookId, reviewData));
    if (data?.errors) {
      setErrors(data?.errors);
    } else {
      dispatch(getAllReviews(bookId)).then(closeModal());
    }
  };

  return (
    <div className="create-review-modal--container">
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
              defaultChecked
              onChange={() => setSpoiler(false)}
            />
          </label>
        </div>
        {errors.spoiler && <p className="errors">{errors.spoiler}</p>}
        <div className="create-review-modal--stars">
          <div
            className={
              rating >= 1
                ? "create-review-modal--rating-filled"
                : "create-review-modal--rating-empty"
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
                ? "create-review-modal--rating-filled"
                : "create-review-modal--rating-empty"
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
                ? "create-review-modal--rating-filled"
                : "create-review-modal--rating-empty"
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
                ? "create-review-modal--rating-filled"
                : "create-review-modal--rating-empty"
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
                ? "create-review-modal--rating-filled"
                : "create-review-modal--rating-empty"
            }
          >
            <i
              className="fa-solid fa-star "
              onMouseEnter={() => setRating(5)}
            ></i>
          </div>
        </div>
        {errors.rating && <p className="errors">{errors.rating}</p>}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default CreateReviewModal;
