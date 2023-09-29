import React, { useEffect } from "react";
import { NavLink } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import LogoComponent from "../Logo";
import NavSearchBar from "../NavSearchBar";
import { getAllBooks } from "../../store/books";
import { comingSoon } from "../../Resources/helperFunctions";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllBooks());
  }, [dispatch]);

  return (
    <div className="navigation--main">
      <div className="main-navigation--container">
        <div className="main-navigation--logo">
          <NavLink exact to="/">
            <LogoComponent />
          </NavLink>
        </div>

        <div className="main-navigation--searchbar">
          <NavSearchBar />
        </div>
        <div className="main-navigation--little-buttons">
          <div className="main-navigation--profile-button">
            <ProfileButton user={sessionUser} />
          </div>{" "}
          <div className="main-navigation--wishlist">
            <button onClick={comingSoon}>
              <i className="fa-solid fa-heart"></i>
            </button>
          </div>
          <i
            className="fa-solid fa-cart-shopping fa-lg main-navigation--cart"
            onClick={comingSoon}
          ></i>
        </div>
      </div>
      <div className="main-navigation--clickable-nav">
        <span onClick={comingSoon}> Books </span>
        {"  ||  "}
        <span onClick={comingSoon}> Fiction </span>
        {"  ||  "}
        <span onClick={comingSoon}> Nonfiction </span>
        {"  ||  "}
        <span onClick={comingSoon}> eBooks </span>
        {"  ||  "}
        <span onClick={comingSoon}> Audiobooks </span>
        {"  ||  "}
        <span onClick={comingSoon}> Teens & YA </span>
        {"  ||  "}
        <span onClick={comingSoon}> Kids </span>
        {"  ||  "}
        <span onClick={comingSoon}> Music & Movies </span>
      </div>
    </div>
  );
}

export default Navigation;
