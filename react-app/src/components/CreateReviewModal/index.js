import { useSelector } from "react-redux";
import "./CreateReviewModal.css";
import React, { useState } from "react";

const CreateReviewModal = ({ user }) => {
  const [pen_name, setPenName] = useState(user?.firstName || null);
  const [rating, setRating] = useState(null);
  const [review, setReview] = useState("");
  const [spoiler, setSpoiler] = useState(false);

  return (
    <div className="create-review-modal--container">
      <h3>Create Review Modal</h3>
      <form>
        <label htmlFor="penName">
          Would you like to use a pen name?
          <input
            id="penName"
            type="text"
            value=""
            onChange={(e) => setPenName(e.target.value)}
          />
        </label>
        <label htmlFor="review">
          How did you like the book?
          <textarea
            id="review"
            value={review}
            onChange={(e) => setReview(e.target.value)}
          />
        </label>
        <label htmlFor="spoiler">
          Does your review contain spoilers?
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
        </label>
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
      </form>
    </div>
  );
};

export default CreateReviewModal;
