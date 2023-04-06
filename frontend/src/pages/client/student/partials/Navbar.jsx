import React, { Component } from 'react';
import { ArrowDownThin, Bell, Cap, Plus, Search } from '../../../../components/Icons';
import student from '../../../../assets/images/student.png';
import teacher from '../../../../assets/images/teacher.webp';

class NotificationsSection extends Component {
    state = {
        active_tab: "general",
        active_tab_class: "text-black border-b-2 border-black font-bold",
        tab_class: "hover:text-black hover:border-b-2 relative z-10 transition-all hover:border-black pb-3",
        tabs:[
            {
                text:"عام",
                id:"general",
                count:2
            },
            {
                text:"النظام",
                id:"system",
                count:1,
            },
            {
                text:"الجامعة",
                id:"org",
                count:0,
            }
        ]
    }
    change_tab = (e) =>{
        this.setState({
            active_tab:e.target.id
        })
    }


    get_tabs = () => {

        return (

            <div className="notifications--header p-5 text-xs grid grid-cols-3 text-center text-gray-500">
                {/* tabs */}
                {this.state.tabs.map(ele=>{
                    return <button id={ele.id} onClick={this.change_tab} key={ele.id} className={`${this.state.tab_class} ${this.state.active_tab == ele.id ? this.state.active_tab_class : '' }`}>
                        {ele.text}
                        {ele.count ? <span id={ele.id} className="absolute font-light text-xs  w-4 h-4 rounded-full bg-red-500 text-white"> {ele.count} </span> : ''}
                     </button>
                })}
            </div>
        );
    }


    render() {
        return (
            <div className='relative  z-20'>

                <span className="w-5 h-5  t-center text-xs p-0 m-0 absolute left-0 -top-[10px] bg-red-500 text-white rounded-full">2</span>
                <Bell className='w-6 h-6 peer' />
                <div className="account--notifications hidden hover:block  peer-hover:block alex text-xs pt-10 absolute  -right-96 top-3  w-[400px] min-h-[450px]">

                    <div className="w-full shadow bg-white   rounded">
                        <h1 className='p-3 pt-5 bg-gray-500 rounded text-white border-gray-500 border alex text-base flex gap-x-3'> <Bell className='w-6 h-6' /> الأشعارات</h1>
                        {/* Tabs */}
                        {this.get_tabs()}
                        <div className=" notifications-body h-96 overflow-auto">
                            <ul id='general' className={`${this.state.active_tab == "general" ? "block" : "hidden"} transition-all`}>
                                <li className='grid p-3 hover:bg-gray-50 transition-all grid-cols-12  gap-x-3 items-start'>
                                    <div className="col-span-3 flex  gap-x-2 justify-center items-center">

                                        <img src={teacher} alt="" className="w-10 object-cover h-10 bg-gray-100 rounded-full" />
                                    </div>
                                    <div className=' col-span-9'>
                                        <div className='font-bold  [line-height:25px]'>
                                            <div className="w-1 h-1 bg-gray-500 rounded-full"></div>
                                            أستاذ محمد عباس
                                            <span className=' font-normal text-gray-500 '> اضاف ملخص جديد لمادة <span className='underline'> الرياضيات </span>  </span>
                                            <button className="bg-gray-100  text-xs w-fit font-normal p-2 rounded"> ملخص الشهر الثالث .pdf  </button>
                                            <br />
                                            <sub className='text-gray-500'>  منذ 5 ساعات  </sub>
                                        </div>

                                    </div>

                                </li>
                            </ul>
                            <ul id='system' className={`${this.state.active_tab == "system" ? "block" : "hidden"} transition-all`}>
                                <li className='grid p-3 hover:bg-gray-50 transition-all grid-cols-12  gap-x-3 items-start'>
                                    <div className="col-span-3 flex  gap-x-2 justify-center items-center">

                                        <img src={teacher} alt="" className="w-10 object-cover h-10 bg-gray-100 rounded-full" />
                                    </div>
                                    <div className=' col-span-9'>
                                        <div className='font-bold  [line-height:25px]'>
                                            <div className="w-1 h-1 bg-gray-500 rounded-full"></div>
                                            أستاذ محمد عباس
                                            <span className=' font-normal text-gray-500 '> اضاف ملخص جديد لمادة <span className='underline'> الرياضيات </span>  </span>
                                            <button className="bg-gray-100  text-xs w-fit font-normal p-2 rounded"> ملخص الشهر الثالث .pdf  </button>
                                            <br />
                                            <sub className='text-gray-500'>  منذ 5 ساعات  </sub>
                                        </div>

                                    </div>

                                </li>
                                <li className='grid p-3 hover:bg-gray-50 transition-all grid-cols-12  gap-x-3 items-start'>
                                    <div className="col-span-3 flex  gap-x-2 justify-center items-center">

                                        <img src={teacher} alt="" className="w-10 object-cover h-10 bg-gray-100 rounded-full" />
                                    </div>
                                    <div className=' col-span-9'>
                                        <div className='font-bold  [line-height:25px]'>
                                            <div className="w-1 h-1 bg-gray-500 rounded-full"></div>
                                            أستاذ محمد عباس
                                            <span className=' font-normal text-gray-500 '> اضاف ملخص جديد لمادة <span className='underline'> الرياضيات </span>  </span>
                                            <button className="bg-gray-100  text-xs w-fit font-normal p-2 rounded"> ملخص الشهر الثالث .pdf  </button>
                                            <br />
                                            <sub className='text-gray-500'>  منذ 5 ساعات  </sub>
                                        </div>

                                    </div>

                                </li>
                            </ul>
                            <ul id='org' className={`${this.state.active_tab == "org" ? "block" : "hidden"} transition-all`}>
                                <li className='grid p-3 hover:bg-gray-50 transition-all grid-cols-12  gap-x-3 items-start'>
                                    <div className="col-span-3 flex  gap-x-2 justify-center items-center">

                                        <img src={teacher} alt="" className="w-10 object-cover h-10 bg-gray-100 rounded-full" />
                                    </div>
                                    <div className=' col-span-9'>
                                        <div className='font-bold  [line-height:25px]'>
                                            <div className="w-1 h-1 bg-gray-500 rounded-full"></div>
                                            أستاذ محمد عباس
                                            <span className=' font-normal text-gray-500 '> اضاف ملخص جديد لمادة <span className='underline'> الرياضيات </span>  </span>
                                            <button className="bg-gray-100  text-xs w-fit font-normal p-2 rounded"> ملخص الشهر الثالث .pdf  </button>
                                            <br />
                                            <sub className='text-gray-500'>  منذ 5 ساعات  </sub>
                                        </div>

                                    </div>

                                </li>
                                <li className='grid p-3 hover:bg-gray-50 transition-all grid-cols-12  gap-x-3 items-start'>
                                    <div className="col-span-3 flex  gap-x-2 justify-center items-center">

                                        <img src={teacher} alt="" className="w-10 object-cover h-10 bg-gray-100 rounded-full" />
                                    </div>
                                    <div className=' col-span-9'>
                                        <div className='font-bold  [line-height:25px]'>
                                            <div className="w-1 h-1 bg-gray-500 rounded-full"></div>
                                            أستاذ محمد عباس
                                            <span className=' font-normal text-gray-500 '> اضاف ملخص جديد لمادة <span className='underline'> الرياضيات </span>  </span>
                                            <button className="bg-gray-100  text-xs w-fit font-normal p-2 rounded"> ملخص الشهر الثالث .pdf  </button>
                                            <br />
                                            <sub className='text-gray-500'>  منذ 5 ساعات  </sub>
                                        </div>

                                    </div>

                                </li>
                                <li className='grid p-3 hover:bg-gray-50 transition-all grid-cols-12  gap-x-3 items-start'>
                                    <div className="col-span-3 flex  gap-x-2 justify-center items-center">

                                        <img src={teacher} alt="" className="w-10 object-cover h-10 bg-gray-100 rounded-full" />
                                    </div>
                                    <div className=' col-span-9'>
                                        <div className='font-bold  [line-height:25px]'>
                                            <div className="w-1 h-1 bg-gray-500 rounded-full"></div>
                                            أستاذ محمد عباس
                                            <span className=' font-normal text-gray-500 '> اضاف ملخص جديد لمادة <span className='underline'> الرياضيات </span>  </span>
                                            <button className="bg-gray-100  text-xs w-fit font-normal p-2 rounded"> ملخص الشهر الثالث .pdf  </button>
                                            <br />
                                            <sub className='text-gray-500'>  منذ 5 ساعات  </sub>
                                        </div>

                                    </div>

                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

}

class NavBar extends Component {
    state = {}
    render() {
        return (
            <div className='dashboard--navbar flex items-center justify-between'>
                {/* links */}
                <div className="navbar--links">
                    <div className="navbar--search flex items-center relative z-10">
                        <span className='absolute left-3  text-gray-400'><Search className="w-5 h-5" /></span>
                        <input placeholder='ابحث ' type="text" className='bg-gray-100 text-sm focus:w-[500px] transition-all focus:outline-none px-5 text-gray-500   placeholder:text-gray-400 w-80 p-2 rounded-full' name="search" id="search" />
                    </div>
                </div>
                {/* account  */}
                <div className="navbar--account  ">
                    {/* adding summary button */}
                    <button className="bg-gray-500 min-w-fit flex items-center justify-between gap-x-3 add--summary--button ml-10 text-white py-1 px-2 text-xs rounded"> اضافة ملخص  <Plus className='w-5 h-5' /> </button>
                    {/* notifications */}
                    <NotificationsSection />
                    <div className=" flex items-center justify-end h-full text-gray-800 account--profile">
                        <ArrowDownThin className='w-4 h-4 cursor-pointer' />
                        <div>
                            <span className='text-xs font-bold'> Alaa Ali </span>
                            <p className='text-[10px] text-gray-500'> alaaali@ </p>

                        </div>
                        <div className=" ">
                            <img alt='user' src={student} className='shadow  w-10 h-10 bg-gray-100 rounded-full' />
                        </div>

                    </div>


                </div>

            </div>
        );
    }
}

export default NavBar;