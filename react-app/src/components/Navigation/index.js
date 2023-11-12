import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import LogoComponent from "../Logo";
import NavSearchBar from "../NavSearchBar";
import { getAllBooks } from "../../store/books";
import { comingSoon } from "../../Resources/helperFunctions";
import WishlistDropdown from "./WishlistDropdown.js";
import FictionDropdown from "./FictionDropdown.js";
import NonfictionDropdown from "./NonfictionDropdown.js";
import BooksDropdown from "./BooksDropdown.js";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const [showFiction, setShowFiction] = useState(false);
  const [showNonfiction, setShowNonfiction] = useState(false);
  const [showBooks, setShowBooks] = useState(false);

  useEffect(() => {
    dispatch(getAllBooks());
  }, [dispatch]);

  //----------------Show dropdowns helper functions--------------------

  //-------------------------------------------------------------------

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
            <WishlistDropdown user={sessionUser} />
          </div>
          <i
            className="fa-solid fa-cart-shopping fa-lg main-navigation--cart"
            onClick={comingSoon}
          ></i>
        </div>
      </div>
      <div className="main-navigation--clickable-nav">
        <span
          className="main-navigation--clickable-nav-category"
          onMouseEnter={() => setShowBooks(true)}
          onMouseLeave={() => setShowBooks(false)}
        >
          {" "}
          Books{" "}
          {showBooks ? (
            <span>
              <BooksDropdown />
            </span>
          ) : null}
        </span>
        {"  ||  "}
        <span
          className="main-navigation--clickable-nav-category"
          onMouseEnter={() => setShowFiction(true)}
          onMouseLeave={() => setShowFiction(false)}
        >
          {" "}
          Fiction{" "}
          {showFiction ? (
            <span>
              <FictionDropdown />
            </span>
          ) : null}
        </span>
        {"  ||  "}
        <span
          className="main-navigation--clickable-nav-category"
          onMouseEnter={() => setShowNonfiction(true)}
          onMouseLeave={() => setShowNonfiction(false)}
        >
          {" "}
          Nonfiction{" "}
          {showNonfiction ? (
            <span>
              <NonfictionDropdown />
            </span>
          ) : null}
        </span>
        {"  ||  "}
        <span
          className="main-navigation--clickable-nav-category"
          onClick={comingSoon}
        >
          {" "}
          eBooks{" "}
        </span>
        {"  ||  "}
        <span
          className="main-navigation--clickable-nav-category"
          onClick={comingSoon}
        >
          {" "}
          Audiobooks{" "}
        </span>
        {"  ||  "}
        <span
          className="main-navigation--clickable-nav-category"
          onClick={comingSoon}
        >
          {" "}
          Teens & YA{" "}
        </span>
        {"  ||  "}
        <span
          className="main-navigation--clickable-nav-category"
          onClick={comingSoon}
        >
          {" "}
          Kids{" "}
        </span>
        {"  ||  "}
        <span
          className="main-navigation--clickable-nav-category"
          onClick={comingSoon}
        >
          {" "}
          Music & Movies{" "}
        </span>
      </div>
    </div>
  );
}

export default Navigation;
