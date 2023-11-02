import { useEffect } from "react";
import "./WishlistDetail.css";
import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import {
  clearCurrentWishlist,
  currentWishlist,
  getWishlistById,
} from "../../store/wishlists";
import LoadingSpinner from "../LoadingSpinner";
import { useHistory, Redirect } from "react-router-dom";
import { useModal } from "../../context/Modal";
import DeleteWishlistModal from "../DeleteWishlistModal";

const WishlistDetail = () => {
  const { wishlistId } = useParams();
  const dispatch = useDispatch();
  const wishlist = useSelector(currentWishlist).Books;
  const wishlistInfo = useSelector(currentWishlist).Wishlist;
  const history = useHistory();
  const { setModalContent } = useModal();
  const user = useSelector((state) => state.session.user);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setIsLoading(true);
    dispatch(getWishlistById(wishlistId)).then(() => setIsLoading(false));

    return () => {
      dispatch(clearCurrentWishlist());
    };
  }, [dispatch, wishlistId]);

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
      {wishlist.map((book) => (
        <li key={book.id}>{book.title}</li>
      ))}
    </div>
  );
};

export default WishlistDetail;
