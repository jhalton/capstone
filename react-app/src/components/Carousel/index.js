import "./Carousel.css";
import React, { useState, useEffect } from "react";

export const CarouselItem = ({ children, width }) => {
  return (
    <div className="carousel-item" style={{ width: width }}>
      {children}
    </div>
  );
};

const Carousel = ({ children }) => {
  const [activeIndex, setActiveIndex] = useState(0);
  const [paused, setPaused] = useState(false);

  //   useEffect(() => {
  //     const interval = setInterval(() => {
  //       if (!paused) {
  //         updateIndex(activeIndex + 1);
  //       }
  //     }, 3000);

  //     return () => {
  //       if (interval) {
  //         clearInterval();
  //       }
  //     };
  //   });

  const updateIndex = (newIndex) => {
    if (newIndex < 0) {
      newIndex = React.Children.count(children - 1);
    } else if (newIndex >= React.Children.count(children)) {
      newIndex = 0;
    }
    setActiveIndex(newIndex);
  };

  return (
    <div
      className="carousel"
      onMouseEnter={() => setPaused(true)}
      onMouseLeave={() => setPaused(false)}
    >
      <div
        className="carousel-inner"
        style={{ transform: `translateX(-${activeIndex * 100}%)` }}
      >
        {React.Children.map(children, (child, index) => {
          return React.cloneElement(child, { width: "100%" });
        })}
      </div>
      <div className="carousel--indicators">
        <button onClick={() => updateIndex(activeIndex - 1)}>
          <i
            className="fa-solid fa-angle-left"
            style={{ color: "#000000" }}
          ></i>
        </button>
        <button onClick={() => updateIndex(activeIndex + 1)}>
          <i
            className="fa-solid fa-angle-right"
            style={{ color: "#000000" }}
          ></i>
        </button>
      </div>
    </div>
  );
};

export default Carousel;
