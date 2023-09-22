import "./NavSearchBarDropdown.css";
import React from "react";
import { useHistory } from "react-router-dom";

const NavSearchBarDropdown = ({ populate, setSearch }) => {
  const history = useHistory();

  return (
    <div className="nav-search-bar-dropdown--container">
      {populate ? (
        populate.length ? (
          populate.map((item) => (
            <li
              key={item.id}
              value={item}
              className="nav-search-bar-dropdown--li"
              onClick={() => history.push(`/books/${item.id}`) && setSearch("")}
            >
              <div className="nav-search-bar-dropdown--searchtile">
                <p>
                  {item.title} by {item.authorFirstName} {item.authorLastName}
                </p>
              </div>
            </li>
          ))
        ) : (
          <p>No matches found</p>
        )
      ) : (
        ""
      )}
    </div>
  );
};

export default NavSearchBarDropdown;
