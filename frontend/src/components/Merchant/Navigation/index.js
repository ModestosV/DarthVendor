// import axios from 'axios';
// import React, {Component} from 'react';
// import {Link, withRouter} from 'react-router-dom';
// import settings from '../../config/settings';
// import './Navigation.scss';


// class Navigation extends Component {

//     handleLogOutButton() {
//         const {history} = this.props;
//         let headers = {
//             'authorization': JSON.parse(localStorage.activeUser)['token'] 
//         };        
//         let config = {
//             'headers': headers
//         };
        
//         axios.get(`${settings.API_ROOT}/logout`, config)
//             .then(response => {
//                 console.log(response);
//                 localStorage.setItem('activeUser', '');
//                 history.push('/login');
//             })
//             .catch(error => {
//                 console.log(error);                
//             })
//     }

//     renderToggleButton() {
//         return (
//             <button className="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#myNavbar" aria-controls="myNavbar" aria-expanded="false" aria-label="Toggle navigation">
//                 <span className="navbar-toggler-icon"></span>
//             </button>   
//         )
//     }

//     renderLogOutButton() {
//         return (
//             <ul className="navbar-nav">
//                 <li className="nav-item">
//                     <button 
//                         className="btn btn-danger"
//                         onClick={() => this.handleLogOutButton()}
//                     >
//                         Log Out
//                         {" "} 
//                         <i className="fa fa-sign-out" aria-hidden="true"></i>                                                
//                     </button>
//                 </li>        
//             </ul>
//         )
//     }

//     render() {
//         return (    
//             <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
//                 <a className="navbar-brand" href="#">DarthVendor </a>

//                 {this.renderToggleButton()}
                
//                 <div className="navbar-collapse collapse" id="myNavbar">
//                     <ul className="navbar-nav mr-auto">
//                         <li className="nav-item active">
//                             <Link className="nav-link" to={`/`}>
//                                 <i className="fa fa-list-alt" aria-hidden="true"></i>
//                                 {" "} Home 
//                                 <span className="sr-only">(current)</span>
//                             </Link>
//                         </li>
//                         <li className="nav-item">
//                             <Link className="nav-link" to={`/catalog`}>
//                                 <i className="fa fa-folder" aria-hidden="true"></i>                            
//                                 {" "} Catalog
//                             </Link>
//                         </li>                                                
//                     </ul>   

//                     {this.renderLogOutButton()}
//                 </div>
//             </nav>         
//         )
//     }
// }

// export default withRouter(Navigation);