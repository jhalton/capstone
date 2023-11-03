import "./RemoveBookFromWishlistModal.css";
import React from "react";
import { useDispatch } from "react-redux";
import { deleteBookFromWishlist, getWishlistById } from "../../store/wishlists";
import { useModal } from "../../context/Modal";

const RemoveBookFromWishlistModal = ({ wishlist, bookId }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();

  const handleRemoveFromWishlist = (bookId) => {
    dispatch(deleteBookFromWishlist(wishlist.id, bookId)).then(() =>
      dispatch(getWishlistById(wishlist.id)).then(closeModal())
    );
  };

  const handleKeep = () => {
    closeModal();
  };

  return (
    <div className="remove-book-from-wishlist-modal--container">
      <h3>Remove from wishlist?</h3>
      <div className="remove-book-from-wishlist-modal--buttons">
        <button onClick={() => handleRemoveFromWishlist(bookId)}>Remove</button>
        <button onClick={handleKeep}>Keep</button>
      </div>
    </div>
  );
};

export default RemoveBookFromWishlistModal;
