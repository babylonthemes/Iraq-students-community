import React, { Component } from 'react';
import './DashboardHome.css';
import { Beaker, Building, EnvelopeOpen, Puzzle } from '../../../../components/Icons';
import student from '../../../../assets/images/student.png';

class Summary extends Component {
    state = {
        active_tab: "exams",
        active_tab_class: "text-gray-800 bg-white font-bold",
        tab_class: "text-gray-500 text-center rounded flex gap-x-2 items-center hover:bg-white hover:text-gray-800 p-3 py-3",
        tabs: [
            {
                text: "الامتحانات",
                id: "exams",
                icon: <Puzzle className='w-4 h-4' />
            },
            {
                text: "التحاضير",
                id: "homework",
                icon: <Beaker className='w-4 h-4' />
            },
            {
                text: "التبليغات",
                id: "reports",
                icon: <EnvelopeOpen className='w-4 h-4' />
            }
        ],
        exams: [
            {
                title: "الكيمياء العضوية ",
                id:"chim-exam",
                time: Date.now(),
                caption: "امتحان نهاية السنة ",
                subject: "كيمياء",
                sug: "ملخص دروس الكيمياء العضوية ",
                sug_link:"https://jyal.com/courses/ogranic_chim",
                lesons_link: "https://jyal.com/lesons/organic_chim",
                summary_link: "https://jyal.com/summries/organic_chim",


            }
        ],
        homework: [
            {
                title: "الكيمياء العضوية ",
                id:"chim-homework",
                time: Date.now(),
                caption: "امتحان نهاية السنة ",
                subject: "كيمياء",
                sug: "ملخص دروس الكيمياء العضوية ",
                sug_link:"https://jyal.com/courses/ogranic_chim",
                lesons_link: "https://jyal.com/lesons/organic_chim",
                summary_link: "https://jyal.com/summries/organic_chim",


            }
        ],   
        reports: [
            {
                title: "الكيمياء العضوية ",
                id:"chim-reports",
                time: Date.now(),
                caption: "امتحان نهاية السنة ",
                subject: "كيمياء",
                sug: "ملخص دروس الكيمياء العضوية ",
                sug_link:"https://jyal.com/courses/ogranic_chim",
                lesons_link: "https://jyal.com/lesons/organic_chim",
                summary_link: "https://jyal.com/summries/organic_chim",


            }
        ], 
    }


    get_exams = () => {

        return (
            <ul id='exams' className={` ${this.state.active_tab == "exams" ? "block" : "hidden"} transition-all   grid grid-cols-3 gap-3`}>
                {this.state.exams.map(ele => {
                    return <li  key={ele.id} className="w-full text-gray-800 pt-4  p-2 border border-gray-300 bg-white rounded">
                        <div className="bg-gray-500 w-fit text-[8px] px-3 p-1 text-white rounded-full"> {ele.subject}  </div>
                        <div className='mt-3 p-5'>
                            <span className='font-light opacity-70'> امتحان  </span>
                            <span className='text-base'> {ele.title} </span>
                            <p className="mt-2 text-gray-300 text-xs"> {ele.caption} </p>
                            <div className="mt-5 flex gap-3 items-center">
                                <a href={ele.lesons_link} className="bg-gray-500 rounded-full p-2 text-white text-xs"> مراجعة الدروس </a>
                                <a href={ele.summary_link} className="hover:bg-gray-500 rounded-full p-2 text-gray-500 border border-gray-500 transition hover:text-white text-xs"> قراءة الملخص</a>
                            </div>
                            <a href={ele.sug_link} className=" mt-5 block  text-[10px] text-black"> مقترح <span className='text-gray-600 underline'> {ele.sug} </span> </a>
                        </div>

                    </li>
                })}{

                }
            </ul>
        );

    }


    get_homework = () => {

        return (
            <ul id='homework' className={` ${this.state.active_tab == "homework" ? "block" : "hidden"} transition-all   grid grid-cols-3 gap-3`}>
                {this.state.homework.map(ele => {
                    return <li key={ele.id} className="w-full text-gray-800 pt-4  p-2 border border-gray-300 bg-white rounded">
                        <div className="bg-gray-500 w-fit text-[8px] px-3 p-1 text-white rounded-full"> {ele.subject}  </div>
                        <div className='mt-3 p-5'>
                            <span className='font-light opacity-70'> امتحان  </span>
                            <span className='text-base'> {ele.title} </span>
                            <p className="mt-2 text-gray-300 text-xs"> {ele.caption} </p>
                            <div className="mt-5 flex gap-3 items-center">
                                <a href={ele.lesons_link} className="bg-gray-500 rounded-full p-2 text-white text-xs"> مراجعة الدروس </a>
                                <a href={ele.summary_link} className="hover:bg-gray-500 rounded-full p-2 text-gray-500 border border-gray-500 transition hover:text-white text-xs"> قراءة الملخص</a>
                            </div>
                            <a href={ele.sug_link} className=" mt-5 block  text-[10px] text-black"> مقترح <span className='text-gray-600 underline'> {ele.sug} </span> </a>
                        </div>

                    </li>
                })}{

                }
            </ul>
        );

    }


    get_reports = () => {

        return (
            <ul id='reports' className={` ${this.state.active_tab == "reports" ? "block" : "hidden"} transition-all   grid grid-cols-3 gap-3`}>
                {this.state.homework.map(ele => {
                    return <li key={ele.id} className="w-full text-gray-800 pt-4  p-2 border border-gray-300 bg-white rounded">
                        <div className="bg-gray-500 w-fit text-[8px] px-3 p-1 text-white rounded-full"> {ele.subject}  </div>
                        <div className='mt-3 p-5'>
                            <span className='font-light opacity-70'> امتحان  </span>
                            <span className='text-base'> {ele.title} </span>
                            <p className="mt-2 text-gray-300 text-xs"> {ele.caption} </p>
                            <div className="mt-5 flex gap-3 items-center">
                                <a href={ele.lesons_link} className="bg-gray-500 rounded-full p-2 text-white text-xs"> مراجعة الدروس </a>
                                <a href={ele.summary_link} className="hover:bg-gray-500 rounded-full p-2 text-gray-500 border border-gray-500 transition hover:text-white text-xs"> قراءة الملخص</a>
                            </div>
                            <a href={ele.sug_link} className=" mt-5 block  text-[10px] text-black"> مقترح <span className='text-gray-600 underline'> {ele.sug} </span> </a>
                        </div>

                    </li>
                })}{

                }
            </ul>
        );

    }

    change_tab = (e) => {
        this.setState({
            active_tab: e.target.id
        })
    }


    get_tabs = () => {

        return (

            <div className="summary--header  w-fit p-2  text-xs bg-gray-50   rounded   flex items-center gap-x-2">
                {/* tabs */}
                {this.state.tabs.map(ele => {
                    return <button id={ele.id} onClick={this.change_tab} key={ele.id} className={`${this.state.tab_class} ${this.state.active_tab == ele.id ? this.state.active_tab_class : ''} `}>
                        {ele.text}
                    </button>
                })}
            </div>
        );
    }

    render() {
        return (

            <div className="lg:col-span-7  overflow-auto   " >
                <div className="grid   rounded  overflow-hidden">
                    {/* summary header */}
                    {this.get_tabs()}
                    {/* summary header end */}
                    {/* summary body */}
                    <div className="p-3  mt-5 relative z-10">
                        {/* exams summary */}
                            {this.get_exams()}
                        {/* exams summary end */}
                        {/* Homework summary */}
                        {this.get_homework()}
                        {/* Homework summary end */}
                        {/* Reports summary */}
                        {this.get_reports()}
                        {/* Reports summary end */}
                    </div>

                    {/* summary body end */}
                </div>
            </div>

        );
    }
}

class Home extends Component {
    state = {
        study: 97,
        exp: 1500,
        coins: 1550

    }
    render() {
        return (
            <main className='grid gap-5  student--home--container'>
                <div className="grid lg:grid-cols-10 gap-5">

                    {/* Profile */}
                    <div className='lg:col-span-3 border-l pl-5 sm:rtl ltr flex flex-col gap-y-5 '>
                        <div className=" grid justify-center h-fit  p-5  bg-white shadow-md rounded ">
                            <div className='w-full items-center text-center flex flex-col gap-y-4'>
                                <img alt='Alaa Ali' src={student} className="t-cneter object-cover w-32 h-32 bg-white rounded-full" />
                                <div>
                                    <h1 className='text-xl font-bold'> Alaa Ali </h1>
                                    <span className='text-gray-500 text-sm flex gap-x-2'> <Building className='w-5 h-5' /> جامعة باب الزبير , ادارة واقتصاد , مرحلة رابعة </span>
                                </div>
                                <div className="my-2 border-t  w-full"></div>
                                <ul className="grid grid-cols-3">
                                    <li className="w-full text-xs  p-2 gap-y-3  justify-center text-center flex flex-col items-center text-gray-500">
                                        المعدل الدراسي
                                        <span className='text-xl text-black'> {this.state.study}<sub>%</sub></span>
                                    </li>
                                    <li className="w-full text-xs  p-2 gap-y-3  justify-center text-center flex flex-col items-center text-gray-500">
                                        النقاط
                                        <span className='text-xl text-black'> {this.state.coins} </span>
                                    </li>
                                    <li className="w-full text-xs  p-2 gap-y-3  justify-center text-center flex flex-col items-center text-gray-500">
                                        المساهمات
                                        <span className='text-xl text-black'> {this.state.exp}<sub>exp</sub> </span>
                                    </li>
                                </ul>
                                <button className="w-fit m-auto my-2 rounded p-2 bg-gray-500 text-white"> تعديل الحساب </button>
                            </div>

                        </div>
                        {/* course card  */}
                        <div className="w-full flex items-center justify-center course--promo rounded bg-white h-56 shadow-md">
                            <div className="bg-white shadow-md  flex items-center justify-center text-center p-3 font-bold text-xl text-gray-500 rounded w-[85%] h-[70%]">
                                <div>
                                    <h1> لا تفوت فرصة الانضمام الى دروس الكيمياء  </h1>
                                    <button className="text-sm p-2 rounded w-fit m-auto mt-2 hover:text-white hover:bg-gray-500 transition-all text-gray-500 border-2 border-gray-500">انضم الأن</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    {/*  profile end */}
                    {/* summary */}
                    <Summary />
                    {/* summary end */}
                </div>
                <div className="grid w-full h-96 bg-gray-100"></div>
            </main>
        );
    }
}

export default Home;