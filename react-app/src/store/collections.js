//--------------------------------Constants-----------------------------------
const GET_COLLECTIONS = "collections/GET_COLLECTIONS";
const GET_ONE_COLLECTION = "collections/GET_ONE_COLLECTION";
const ADD_COLLECTION = "collections/ADD_COLLECTION";
const REMOVE_COLLECTION = "collections/REMOVE_COLLECTION";
const CLEAR_ONE_COLLECTION = "collections/CLEAR_ONE_COLLECTION";
const CLEAR_ALL_COLLECTIONS = "collections/CLEAR_ALL_COLLECTIONS";

//-----------------------------Action Creators--------------------------------
const getCollections = (collection) => {
  return {
    type: GET_COLLECTIONS,
    payload: collection,
  };
};

const getOneCollection = (collection) => {
  return {
    type: GET_ONE_COLLECTION,
    payload: collection,
  };
};

const addCollection = (collection) => {
  return {
    type: ADD_COLLECTION,
    payload: collection,
  };
};

const removeCollection = (collection) => {
  return {
    type: REMOVE_COLLECTION,
    payload: collection,
  };
};

export const clearOneCollection = () => {
  return {
    type: CLEAR_ONE_COLLECTION,
  };
};

export const clearAllCollections = () => {
  return {
    type: CLEAR_ALL_COLLECTIONS,
  };
};

//---------------------------Thunk Action Creators----------------------------
export const getAllCollections = () => async (dispatch) => {
  const response = await fetch("/api/collections");

  if (response.ok) {
    const data = await response.json();
    dispatch(getCollections(data));
    return data;
  } else if (response.status < 500) {
    const data = (await response).json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const getCollectionById = (collectionId) => async (dispatch) => {
  const response = await fetch(`/api/collections/${collectionId}`);

  if (response.ok) {
    const data = await response.json();
    dispatch(getOneCollection(data));
    return data;
  } else if (response.status < 500) {
    const data = (await response).json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const createCollection = (collection) => async (dispatch) => {
  const response = await fetch(`/api/collections/new`, {
    method: "POST",
    body: collection,
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(addCollection(data));
    return data;
  } else if (response.status < 500) {
    const data = (await response).json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

export const editCollection =
  (collectionId, collection) => async (dispatch) => {
    const response = await fetch(`/api/collections/${collectionId}/edit`, {
      method: "PUT",
      body: collection,
    });
    if (response.ok) {
      const data = await response.json();
      dispatch(addCollection(data));
      return data;
    } else if (response.status < 500) {
      const data = (await response).json();
      return data.errors;
    } else {
      return ["Oops! An error occurred. Please try again."];
    }
  };

export const deleteCollection = (collectionId) => async (dispatch) => {
  const response = await fetch(`/api/collections/${collectionId}/delete`, {
    method: "DELETE",
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(removeCollection(data));
    return data;
  } else if (response.status < 500) {
    const data = (await response).json();
    return data.errors;
  } else {
    return ["Oops! An error occurred. Please try again."];
  }
};

//--------------------------State Selectors--------------------------------
export const allCollections = (state) =>
  Object.values(state.collection.allCollections);
export const currentCollection = (state) => state.collection.currentCollection;
//------------------------------Reducers------------------------------------

const initialState = {
  allCollections: {},
  currentCollection: {},
};

const collectionsReducer = (state = initialState, action) => {
  const newState = { ...state };
  switch (action.type) {
    case GET_COLLECTIONS:
      const allCollections = {};
      action.payload.Collections.forEach((collection) => {
        allCollections[collection.id] = collection;
      });
      return { ...newState, allCollections };
    case GET_ONE_COLLECTION:
      return { ...newState, currentCollection: action.payload };
    case ADD_COLLECTION:
      return {
        ...newState,
        allCollections: {
          [action.payload.id]: action.payload,
        },
      };
    case REMOVE_COLLECTION:
      delete newState[action.payload.id];
      return newState;
    case CLEAR_ALL_COLLECTIONS:
      return { ...newState, allCollections: {} };
    case CLEAR_ONE_COLLECTION:
      return { ...newState, currentCollection: {} };
    default:
      return state;
  }
};

export default collectionsReducer;
