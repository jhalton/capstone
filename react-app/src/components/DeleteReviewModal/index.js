import "./DeleteReviewModal.css";
import React from "react";
import { useDispatch } from "react-redux";
import { deleteReview } from "../../store/reviews";
import { useModal } from "../../context/Modal";

const DeleteReviewModal = ({ review }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();

  const handleDelete = async (e) => {
    e.preventDefault();

    await dispatch(deleteReview(review.id)).then(closeModal());
  };

  return (
    <div className="delete-review-modal--container">
      <h3>Delete Review?</h3>
      <div>
        <button onClick={handleDelete}>Delete</button>
        <button onClick={() => closeModal()}>Keep</button>
      </div>
    </div>
  );
};

export default DeleteReviewModal;
