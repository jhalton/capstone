import "./Navigation.css";
import React, { useState, useEffect, useRef } from "react";
import { useModal } from "../../context/Modal";
import CreateWishlistModal from "../CreateWishlistModal";

const WishlistDropdown = ({ user }) => {
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();
  const { setModalContent } = useModal();

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
            <li>View Wishlists</li>
          </div>
        ) : (
          <span>Log in</span>
        )}
      </ul>
    </>
  );
};

export default WishlistDropdown;
