import { useEffect } from "react";
import "./WishlistDetail.css";
import React from "react-redux";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import {
  clearCurrentWishlist,
  currentWishlist,
  getWishlistById,
} from "../../store/wishlists";
import LoadingSpinner from "../LoadingSpinner";
import { useHistory } from "react-router-dom";

const WishlistDetail = () => {
  const { wishlistId } = useParams();
  const dispatch = useDispatch();
  const wishlist = useSelector(currentWishlist).Books;
  const wishlistInfo = useSelector(currentWishlist).Wishlist;
  const history = useHistory();

  useEffect(() => {
    dispatch(getWishlistById(wishlistId));

    return () => {
      dispatch(clearCurrentWishlist());
    };
  }, [dispatch, wishlistId]);

  if (!wishlist) {
    return <LoadingSpinner />;
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
      {wishlist.map((book) => (
        <li key={book.id}>{book.title}</li>
      ))}
    </div>
  );
};

export default WishlistDetail;
