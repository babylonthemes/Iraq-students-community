import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import ErrorPage from './error-page';
import StudentHome from './pages/client/student/StudentHome';
import Home from './pages/client/student/pages/Home';

const router2 = [
  {
    path:"/new",
    element:<h1> <a href='/new/test'> vist this site  </a> </h1>
  },
  {
    path:"/new/test",
    element:<h1> Hey there  </h1>
  }
];

const router = createBrowserRouter([
  {
    path: "/",
    element: <StudentHome />,
    errorElement:<ErrorPage />,
    children:[
      {
        path:"/",
        element:<Home />
      }
    ],
  },
]);

ReactDOM.render(
  <React.StrictMode>
    <main >
      <RouterProvider router={router} />
    </main>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
