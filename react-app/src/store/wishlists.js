//--------------------------------Constants-----------------------------------
const GET_WISHLISTS = "wishlists/GET_WISHLISTS";
const GET_ONE_WISHLIST = "wishlists/GET_ONE_WISHLIST";
const ADD_WISHLIST = "wishlists/ADD_WISHLIST";
const REMOVE_WISHLIST = "wishlsits/REMOVE_WISHLIST";
const CLEAR_ONE_WISHLIST = "wishlists/CLEAR_ONE_WISHLIST";
const CLEAR_ALL_WISHLISTS = "wishlists/CLEAR_ALL_WISHLISTS";
const ADD_BOOKS_TO_WISHLIST = "wishlists/ADD_BOOKS_TO_WISHLIST";
const REMOVE_BOOKS_FROM_WISHLIST = "wishlists/REMOVE_BOOKS_FROM_WISHLIST";

//-----------------------------Action Creators--------------------------------
const getWishlists = (wishlist) => {
  return {
    type: GET_WISHLISTS,
    payload: wishlist,
  };
};

const getOneWishlist = (wishlist) => {
  return {
    type: GET_ONE_WISHLIST,
    payload: wishlist,
  };
};

const addWishlist = (wishlist) => {
  return {
    type: ADD_WISHLIST,
    payload: wishlist,
  };
};

const removeWishlist = (wishlist) => {
  return {
    type: REMOVE_WISHLIST,
    payload: wishlist,
  };
};

export const clearCurrentWishlist = () => {
  return {
    type: CLEAR_ONE_WISHLIST,
  };
};

export const clearAllWishlists = () => {
  return {
    type: CLEAR_ALL_WISHLISTS,
  };
};

const addToWishlist = (book) => {
  return {
    type: ADD_BOOKS_TO_WISHLIST,
    payload: book,
  };
};

const removeFromWishlist = (book) => {
  return {
    type: REMOVE_BOOKS_FROM_WISHLIST,
    payload: book,
  };
};

//---------------------------Thunk Action Creators----------------------------
export const getAllWishlists = () => async (dispatch) => {
  const response = await fetch("/api/wishlists/all");

  if (response.ok) {
    const data = await response.json();
    dispatch(getWishlists(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const getWishlistById = (wishlistId) => async (dispatch) => {
  const response = await fetch(`/api/wishlists/${wishlistId}`);

  if (response.ok) {
    const data = await response.json();
    dispatch(getOneWishlist(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const createWishlist = (wishlist) => async (dispatch) => {
  const response = await fetch("/api/wishlists/new", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(wishlist),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(addWishlist(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const editWishlist = (wishlistId, wishlist) => async (dispatch) => {
  const response = await fetch(`/api/wishlists/${wishlistId}/edit`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(wishlist),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(addWishlist(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const deleteWishlist = (wishlistId) => async (dispatch) => {
  const response = await fetch(`/api/wishlists/${wishlistId}/delete`, {
    method: "DELETE",
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(removeWishlist(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const addBookToWishlist = (wishlistId, book) => async (dispatch) => {
  const response = await fetch(`/api/wishlists/${wishlistId}/add_books`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ book_ids: [book.id] }),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(addToWishlist(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const deleteBookFromWishlist =
  (wishlistId, bookId) => async (dispatch) => {
    const response = await fetch(
      `/api/wishlists/${wishlistId}/${bookId}/delete`,
      {
        method: "DELETE",
      }
    );

    if (response.ok) {
      const data = await response.json();
      dispatch(removeFromWishlist(data));
      return data;
    } else if (response.status < 500) {
      const data = await response.json();
      return data.errors;
    } else {
      return ["Oops! An error occurred. Please try again."];
    }
  };

//--------------------------State Selectors--------------------------------
export const allWishlists = (state) =>
  Object.values(state.wishlist.allWishlists);
export const currentWishlist = (state) => state.wishlist.currentWishlist;

//------------------------------Reducers------------------------------------
const initialState = {
  allWishlists: {},
  currentWishlist: {},
};

const wishlistsReducer = (state = initialState, action) => {
  const newState = { ...state };
  switch (action.type) {
    case GET_WISHLISTS:
      const allWishlists = {};
      action.payload.Wishlists.forEach((wishlist) => {
        allWishlists[wishlist.id] = wishlist;
      });
      return { ...newState, allWishlists };
    case GET_ONE_WISHLIST:
      return { ...newState, currentWishlist: action.payload };
    case ADD_WISHLIST:
      return {
        ...newState,
        allWishlists: {
          [action.payload.id]: action.payload,
        },
      };
    case REMOVE_WISHLIST:
      delete newState[action.payload.id];
      return newState;
    case ADD_BOOKS_TO_WISHLIST:
      const updatedWishlist = { ...newState.currentWishlist };
      updatedWishlist[action.payload.id] = action.payload;
      return { ...newState, currentWishlist: updatedWishlist };
    case REMOVE_BOOKS_FROM_WISHLIST:
      delete newState.currentWishlist[action.payload.id];
      return newState;
    case CLEAR_ALL_WISHLISTS:
      return { ...newState, allWishlists: {} };
    case CLEAR_ONE_WISHLIST:
      return { ...newState, currentWishlist: {} };
    default:
      return state;
  }
};

export default wishlistsReducer;
