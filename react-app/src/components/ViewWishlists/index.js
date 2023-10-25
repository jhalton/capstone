import "./ViewWishlists.css";
import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { allWishlists, getAllWishlists } from "../../store/wishlists";
import LoadingSpinner from "../LoadingSpinner";
import {
  Redirect,
  useHistory,
} from "react-router-dom/cjs/react-router-dom.min";

const ViewWishlists = () => {
  const dispatch = useDispatch();
  const wishlists = useSelector(allWishlists);
  const user = useSelector((state) => state.session.user);
  const history = useHistory();

  useEffect(() => {
    dispatch(getAllWishlists());
  }, [dispatch]);

  if (!user) {
    return <Redirect to="/" />;
  }

  if (!wishlists) {
    return <LoadingSpinner />;
  }

  return (
    <div className="view-wishlists--container">
      <h1>{user.firstName}'s Wishlists</h1>
      {wishlists.map((wishlist) => (
        <li
          key={wishlist.id}
          onClick={() => history.push(`/wishlists/${wishlist.id}`)}
        >
          {wishlist.name}
        </li>
      ))}
    </div>
  );
};

export default ViewWishlists;
