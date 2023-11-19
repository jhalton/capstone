//------------------------------Constants----------------------------
const GET_REVIEWS = "reviews/GET_REVIEWS";
const GET_ONE_REVIEW = "reviews/GET_ONE_REVIEW";
const ADD_REVIEW = "reviews/ADD_REVIEW";
const REMOVE_REVIEW = "reviews/REMOVE_REVIEW";
const CLEAR_ONE_REVIEW = "reviews/CLEAR_ONE_REVIEW";
const CLEAR_ALL_REVIEWS = "reviews/CLEAR_ALL_REVIEWS";

//---------------------------Action Creators------------------------
const getReviews = (review) => {
  return {
    type: GET_REVIEWS,
    payload: review,
  };
};

const getOneReview = (review) => {
  return {
    type: GET_ONE_REVIEW,
    payload: review,
  };
};

const addReview = (review) => {
  return {
    type: ADD_REVIEW,
    payload: review,
  };
};

const removeReview = (review) => {
  return {
    type: REMOVE_REVIEW,
    payload: review,
  };
};

export const clearCurrentReview = () => {
  return {
    type: CLEAR_ONE_REVIEW,
  };
};

export const clearAllReviews = () => {
  return {
    type: CLEAR_ALL_REVIEWS,
  };
};
//------------------------Thunk Action Creators------------------------------
//Get all reviews
export const getAllReviews = (bookId) => async (dispatch) => {
  const response = await fetch(`/api/books/${bookId}/reviews`);

  if (response.ok) {
    const data = await response.json();
    dispatch(getReviews(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

//Get review by id
export const getReviewById = (reviewId) => async (dispatch) => {
  const response = await fetch(`/api/reviews/${reviewId}`);

  if (response.ok) {
    const data = await response.json();
    dispatch(getOneReview(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

//Create a review
export const createReview = (bookId, review) => async (dispatch) => {
  const response = await fetch(`/api/books/${bookId}/new_review`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(review),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(addReview(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

//Edit a review
export const editReview = (reviewId, review) => async (dispatch) => {
  const response = await fetch(`/api/reviews/${reviewId}/edit`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(review),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(editReview(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

//Delete a review
export const deleteReview = (reviewId) => async (dispatch) => {
  const response = await fetch(`/api/reviews/${reviewId}/delete`, {
    method: "DELETE",
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(removeReview(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

//------------------------State Selectors--------------------------------
export const allReviews = (state) => Object.values(state.review.allReviews);
export const currentReview = (state) => state.review.currentReview;

//-------------------------------Reducers--------------------------------
const initialState = {
  allReviews: {},
  currentReview: {},
};

const reviewsReducer = (state = initialState, action) => {
  const newState = { ...state };
  switch (action.type) {
    case GET_REVIEWS:
      const allReviews = {};
      action.payload.Reviews.forEach((review) => {
        allReviews[review.id] = review;
      });
      return { ...newState, allReviews };
    case GET_ONE_REVIEW:
      return {
        ...newState,
        currentReview: action.payload,
      };
    case ADD_REVIEW:
      return {
        ...newState,
        allReviews: {
          [action.payload.id]: action.payload,
        },
      };
    case REMOVE_REVIEW:
      delete newState[action.payload];
      return newState;
    case CLEAR_ONE_REVIEW:
      return {
        ...newState,
        currentReview: {},
      };
    case CLEAR_ALL_REVIEWS:
      return {
        ...newState,
        allReviews: {},
      };
    default:
      return state;
  }
};

export default reviewsReducer;
