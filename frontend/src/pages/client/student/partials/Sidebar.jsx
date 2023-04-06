import React, { Component } from 'react';
import { Building, Doc, Home, Play } from '../../../../components/Icons';



class SideBar extends Component {
    state = {  } 
    render() { 
        return (
            <div className={`${this.props.className}  lg:sticky h-screen  bg-gray-50  top-0 alex dashboard--sidebar`}>
                <div className="sidebar--container w-full ">
                <h1 className="text-2xl text-center"> جيل </h1>
                <div className="w-full"></div>
                <ul className="sidebar--menu space-y-3  mt-10 text-xs">
                    <li className="   gap-x-2 sidebar--menu--item bg-white  text-gray-500   rounded"> 
                        <Home className='h-5 w-5' />
                        الرئيسية
                     </li>
                     <li className="  sidebar--menu--item  hover:bg-white  hover:text-gray-500 text-gray-500  "> 
                        <Doc className='h-5 w-5' />
                        الملخصات
                     </li>
                     <li className="  sidebar--menu--item  hover:bg-white  hover:text-gray-500  text-gray-500  "> 
                        <Play className='h-5 w-5' />
                        فصل الدراسة
                     </li>
                     <li className="  sidebar--menu--item  hover:bg-white  hover:text-gray-500  text-gray-500  "> 
                        <Building className='h-5 w-5' />
                        التبليغات
                     </li>
                     <li className="  sidebar--menu--item  hover:bg-white  hover:text-gray-500  text-gray-500  "> 
                        <Building className='h-5 w-5' />
                        الدروس التعليمية
                     </li>
                </ul>
                </div>
            </div>
        );
    }
}
 
export default SideBar;