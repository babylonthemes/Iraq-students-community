import React, { Component } from 'react';
import SideBar from './partials/Sidebar';
import NavBar from './partials/Navbar';
import '../Dashboard.css';
import { Outlet } from 'react-router-dom';

class StudentHome extends Component {
    state = {  } 
    render() { 
        return (
            <div className='dashboard--container'>
                <SideBar/>
                <main className='content--container'>
                    <NavBar/>
                    <div className="content">
                        <Outlet />
                    </div>

                </main>

            </div>
        );
    }
}
 
export default StudentHome;