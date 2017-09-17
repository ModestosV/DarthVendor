import {combineReducers} from 'redux';


const rootReducer = combineReducers({
    blank: (state, action) => {if(state == null) state = []; return state;} 
});

export default rootReducer;