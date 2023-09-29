import "./NavSearchBarDropdown.css";
import React from "react";
import { Link } from "react-router-dom";

const NavSearchBarDropdown = ({ populate, closeSearch, search, setSearch }) => {
  return (
    <div className="nav-search-bar-dropdown--container">
      {!populate.length && search ? <p>No matches found</p> : ""}
      {populate.map((item) => (
        <Link
          to={`/books/${item.id}`}
          className="nav-search-bar-dropdown--link"
          onClick={closeSearch}
        >
          <div className="nav-search-bar-dropdown--searchtile">
            <p>
              {item.title} by {item.authorFirstName} {item.authorLastName}
            </p>
          </div>
        </Link>
      ))}
    </div>
  );
};

export default NavSearchBarDropdown;
