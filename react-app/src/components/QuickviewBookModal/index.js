import "./QuickviewBookModal.css";
import React from "react";
import { useModal } from "../../context/Modal";

const QuickviewBookModal = ({ book }) => {
  const { closeModal } = useModal();
  return (
    <div className="quickview-book-modal--container">
      <div className="quickview-book-modal--header-and-close">
        <h3>{book.title}</h3>
        <i className="fa-solid fa-x fa-sm" onClick={() => closeModal()}></i>
      </div>
      <span className="quickview-book-modal--author">
        by {book.authorFirstName} {book.authorLastName}
      </span>
      <span className="quickview-book-modal--description">
        {book.description}
      </span>
    </div>
  );
};

export default QuickviewBookModal;
