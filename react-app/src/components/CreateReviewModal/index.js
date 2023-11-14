import "./CreateReviewModal.css";
import React, { useState } from "react";

const CreateReviewModal = () => {
  const [pen_name, setPenName] = useState(null);
  const [rating, setRating] = useState(null);
  const [review, setReview] = useState("");
  const [spoiler, setSpoiler] = useState(false);
  return (
    <div>
      <h3>Create Review Modal</h3>
      <form>
        <label htmlFor="penName">
          Would you like to use a pen name?
          <input
            id="penName"
            type="text"
            value={pen_name}
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
      </form>
    </div>
  );
};

export default CreateReviewModal;
