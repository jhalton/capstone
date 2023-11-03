import { useEffect } from "react";
import "./WishlistDetail.css";
import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import {
  clearCurrentWishlist,
  currentWishlist,
  deleteBookFromWishlist,
  getWishlistById,
} from "../../store/wishlists";
import LoadingSpinner from "../LoadingSpinner";
import { useHistory, Redirect } from "react-router-dom";
import { useModal } from "../../context/Modal";
import DeleteWishlistModal from "../DeleteWishlistModal";
import RemoveBookFromWishlistModal from "../RemoveBookFromWishlistModal";

const WishlistDetail = () => {
  const { wishlistId } = useParams();
  const dispatch = useDispatch();
  const wishlist = useSelector(currentWishlist).Books;
  const wishlistInfo = useSelector(currentWishlist).Wishlist;
  const history = useHistory();
  const { setModalContent } = useModal();
  const user = useSelector((state) => state.session.user);
  const [isLoading, setIsLoading] = useState(true);
  const [viewIcons, setViewIcons] = useState(null);

  useEffect(() => {
    setIsLoading(true);
    dispatch(getWishlistById(wishlistId)).then(() => setIsLoading(false));

    return () => {
      dispatch(clearCurrentWishlist());
    };
  }, [dispatch, wishlistId]);

  //---------------Show icons helper functions------------------
  const handleMouseEnter = (idx) => {
    setViewIcons(idx);
  };

  const handleMouseLeave = () => {
    setViewIcons(null);
  };

  //--------------------->Icon functions
  const handleNavToBook = (bookId) => {
    history.push(`/books/${bookId}`);
  };

  const handleAddToCart = (bookId) => {
    //This function will both add the item to the cart and remove it from the
    //wishlist.
  };
  //------------------------------------------------------------

  if (isLoading) {
    return <LoadingSpinner />;
  }

  if (user.id !== wishlistInfo?.userId || !wishlistInfo) {
    return <Redirect to="/" />;
  }

  return (
    <div className="wishlist-detail--container">
      <span
        onClick={() => history.push("/wishlists/all")}
        className="wishlist-detail--back-link"
      >
        ← Back to Wishlists
      </span>
      <h1>{wishlistInfo.name}</h1>
      <span
        onClick={() =>
          setModalContent(<DeleteWishlistModal wishlist={wishlistInfo} />)
        }
        className="wishlist-detail--delete-wishlist"
      >
        Delete Wishlist
      </span>
      {wishlist.map((book, idx) => (
        <li
          key={book.id}
          className="wishlist-detail--li"
          onMouseEnter={() => handleMouseEnter(idx)}
          onMouseLeave={handleMouseLeave}
        >
          <img
            className="wishlist-detail--img"
            src={book.frontImage}
            alt={book.title}
          />
          <span
            className={`wishlist-detail--li-functions${
              viewIcons === idx ? " visible" : " hidden"
            }`}
          >
            <i
              class="fa-solid fa-eye "
              onClick={() => handleNavToBook(book.id)}
            ></i>
            <i
              className="fa-solid fa-minus "
              onClick={() =>
                setModalContent(
                  <RemoveBookFromWishlistModal
                    wishlist={wishlistInfo}
                    bookId={book.id}
                  />
                )
              }
            ></i>
            <i className="fa-solid fa-cart-plus "></i>
          </span>
        </li>
      ))}
    </div>
  );
};

export default WishlistDetail;
