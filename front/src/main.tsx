import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { HomePage, ImagesPage, MusicPage } from "./pages";
import "./index.css";

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  },
  {
    path: "/music",
    element: <MusicPage />,
  },
  {
    path: "/images",
    element: <ImagesPage />,
  },
  {
    path: "/test",
    element: <div>aaa</div>,
  },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <div className="bg-[#f5f5f5] h-full p-[16px]">
      <RouterProvider router={router} />
    </div>
  </React.StrictMode>
);
