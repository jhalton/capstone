import "./Navigation.css";
import React, { useState, useEffect, useRef } from "react";
import { useModal } from "../../context/Modal";
import CreateWishlistModal from "../CreateWishlistModal";
import { useHistory } from "react-router-dom";
import LoginFormModal from "../LoginFormModal";

const WishlistDropdown = ({ user }) => {
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();
  const { setModalContent } = useModal();
  const history = useHistory();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const ulClassName = "wishlist-dropdown" + (showMenu ? "" : " hidden");

  return (
    <>
      <i
        className="fa-solid fa-heart wishlist-dropdown--icon"
        onClick={openMenu}
      ></i>
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <div>
            <li onClick={() => setModalContent(<CreateWishlistModal />)}>
              Create Wishlist
            </li>
            <li onClick={() => history.push("/wishlists/all")}>
              View Wishlists
            </li>
          </div>
        ) : (
          <div>
            <span onClick={() => setModalContent(<LoginFormModal />)}>
              Log in
            </span>
          </div>
        )}
      </ul>
    </>
  );
};

export default WishlistDropdown;
