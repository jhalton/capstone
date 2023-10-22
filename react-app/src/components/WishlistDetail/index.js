import { useEffect } from "react";
import "./WishlistDetail.css";
import React from "react-redux";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import { currentWishlist, getWishlistById } from "../../store/wishlists";
import LoadingSpinner from "../LoadingSpinner";

const WishlistDetail = () => {
  const { wishlistId } = useParams();
  const dispatch = useDispatch();
  const wishlist = useSelector(currentWishlist).Books;
  console.log("WISHLIST DETAIL", wishlist);

  useEffect(() => {
    dispatch(getWishlistById(wishlistId));
  }, [dispatch, wishlistId]);

  if (!wishlist) {
    return <LoadingSpinner />;
  }

  return (
    <div>
      <h1>Wishlist Detail Component</h1>
      {wishlist.map((book) => (
        <li key={book.id}>{book.title}</li>
      ))}
    </div>
  );
};

export default WishlistDetail;
