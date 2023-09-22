import React, { useEffect, useState } from "react";
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
      <ul>
        <li>
          <NavLink exact to="/">
            <LogoComponent />
          </NavLink>
        </li>
        {isLoaded && (
          <div className="main-navigation--loaded-div">
            <li>
              <NavSearchBar />
            </li>
            <li>
              <ProfileButton user={sessionUser} />
            </li>
          </div>
        )}
      </ul>
    </div>
  );
}

export default Navigation;
