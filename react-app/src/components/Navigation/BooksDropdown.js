import "./CategoryDropdown.css";
import React from "react";
import { useHistory } from "react-router-dom";

const BooksDropdown = () => {
  const history = useHistory();
  return (
    <div className="category-dropdown--container">
      <span
        className="category-dropdown--genre"
        onClick={() => history.push("/collections")}
      >
        Browse Collections
      </span>
    </div>
  );
};

export default BooksDropdown;
