import axios from 'axios';
import React, {Component} from 'react';
import {Link, withRouter} from 'react-router-dom';
import settings from '../../../../config/settings';
import Sidebar from '../../Sidebar';
import './updatelist.scss'


class UpdateList extends Component {

    constructor(props) {
        super(props);

        this.state = {
            items: [
      
                
                
            ]
        }
    }

    confirmUpdate() {
        swal({
            title: "Apply Updates?",
            text: "Are you sure you want to apply the updates?",            
            type: "warning",
            buttons: {
                confirm:true,
                cancel: true
            }            
          })
          .then((confirm) => {   
              if(confirm){
                console.log('updated');
                window.location = '/'
                  // axios({
                  //     method: 'post',
                  //     url: `${settings.API_ROOT}/item`,
                  //     // withCredentials: true,
                  //     headers: {
                  //         Authorization: "Token " + JSON.parse(localStorage.activeUser).token
                  //     }
                  // })
                  // .then(response => {
                  //     swal("Deleted!", "Your account has been deleted.", "success");
                  // })
                  // .catch(error => {
                  //     console.log(error);
                  //     swal({
                  //         title: "Woops!",
                  //         text: "Something went wrong!",
                  //         ilcon: "error",
                  //         button: "Ok",
                  //     });
                  // })
              }                
          });

    }

    cancelUpdate() {
        swal({
            title: "Cancel updates?",
            text: "Are you sure you want to cancel the updates?",            
            type: "warning",
            buttons: {
                confirm:true,
                cancel: true
            }            
          })
          .then((confirm) => {   
              if(confirm){
                  console.log('canceled');
                  window.location = '/'
                  // axios({
                  //     method: 'post',
                  //     url: `${settings.API_ROOT}/item`,
                  //     // withCredentials: true,
                  //     headers: {
                  //         Authorization: "Token " + JSON.parse(localStorage.activeUser).token
                  //     }
                  // })
                  // .then(response => {
                  //     swal("Deleted!", "Your account has been deleted.", "success");
                  // })
                  // .catch(error => {
                  //     console.log(error);
                  //     swal({
                  //         title: "Woops!",
                  //         text: "Something went wrong!",
                  //         ilcon: "error",
                  //         button: "Ok",
                  //     });
                  // })
              }                
          });
    }

    getUpdateList() {
    //     return axios({
    //         method:'get',
    //         url:`${settings.API_ROOT}/inventory`,
    //         withCredentials: true
    //     })
    //     .then(results => {
    //         const errorMsg = null;
    //         const items = results.data.map(item => item);
    //         this.setState({items});
    //         this.setState({errorMsg});
    //         console.log(items);
    //     })
    //     .catch(error => {
    //      console.log(error);
    //      const errorMsg = "Oops, something went wrong while fetching items!";
    //      this.setState({errorMsg});
    //    })
    }

    // display list of updates
    displayUpdateList() {
        if(this.state.items.length > 0){
            return (                
                <div>
                    {
                        this.state.items.map((item,index) => {
                            return (
                                <div key={index}>
                                    {item.name}
                                </div>
                            );
                        }) 
                    }
                </div>  
            );
        }else{
            return (                
                <div>
                    No items changed.
                </div>  
            );
        }
    }

    displayButtons(){
        if(this.state.items.length > 0){
            return (
                <div className="float-right">
                    <button className="cancel ui button mr-3" onClick={() => {this.cancelUpdate()}}>Cancel</button>
                    <button className="apply ui button mr-3" onClick={() => {this.confirmUpdate()}}>Apply Changes</button>
                </div>
            )
        }
    }


    componentWillMount() {
        console.log(localStorage);
        this.getUpdateList();
       
    }

    render() {
        return (
            <div className="footer">
                <div className="update--list">
                    <h2>Changes</h2>
                    { this.displayUpdateList() }
                </div>
               

               {this.displayButtons()}
            </div>
        )
    }
}

export default UpdateList;
