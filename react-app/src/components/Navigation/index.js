import React, { useEffect } from "react";
import { NavLink } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import LogoComponent from "../Logo";
import NavSearchBar from "../NavSearchBar";
import { getAllBooks } from "../../store/books";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllBooks());
  }, [dispatch]);

  return (
    <div className="main-navigation--container">
      <div className="main-navigation--logo">
        <NavLink exact to="/">
          <LogoComponent />
        </NavLink>
      </div>
      {/* {isLoaded && ( */}{" "}
      <div className="main-navigation--searchbar">
        <NavSearchBar />
      </div>
      <div className="main-navigation--profile-button">
        <ProfileButton user={sessionUser} />
      </div>{" "}
      {/* )} */}
    </div>
  );
}

export default Navigation;
