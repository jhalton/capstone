import "./CategoryDropdown.css";
import React from "react";
import { useHistory } from "react-router-dom";

const TeenYaDropdown = () => {
  const history = useHistory();
  return (
    <div className="category-dropdown--container">
      <span
        className="category-dropdown--genre"
        onClick={() => history.push("/collections/6")}
      >
        Young Adult
      </span>
    </div>
  );
};

export default TeenYaDropdown;
