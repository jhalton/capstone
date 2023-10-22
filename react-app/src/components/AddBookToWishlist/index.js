import "./AddBookToWishlist.css";
import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { addBookToWishlist, allWishlists } from "../../store/wishlists";
import { useModal } from "../../context/Modal";

const AddBookToWishlistModal = ({ book }) => {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const wishlists = useSelector(allWishlists).filter(
    (wishlist) => wishlist.userId === user.id
  );
  const [wishlist, setWishlist] = useState("");
  const { closeModal } = useModal();

  const handleSubmit = (e) => {
    e.preventDefault();

    dispatch(addBookToWishlist(wishlist.id, book));

    closeModal();
  };
  return (
    <div className="add-book-to-wishlist-modal--container">
      <h3>Choose a wishlist:</h3>
      <ul className="add-book-to-wishlist-modal--ul">
        {wishlists.map((wishlist) => (
          <li key={wishlist.id} onClick={() => setWishlist(wishlist)}>
            {wishlist.name}
          </li>
        ))}
      </ul>
      <button onClick={handleSubmit}>Add to Wishlist</button>
    </div>
  );
};

export default AddBookToWishlistModal;
