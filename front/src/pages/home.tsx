import { useNavigate } from "react-router-dom";
import TextLogo from "../assets/logo-text.png";
import { useEffect } from "react";

export const HomePage = () => {
  const navigate = useNavigate();

  useEffect(() => {
    setTimeout(() => {
      navigate("/music");
    }, 2000);
  }, []);

  return (
    <div className="w-[calc(100%+32px)] h-[calc(100%+32px)] flex justify-center items-center bg-black m-[-16px] p-10">
      <img src={TextLogo} className="mb-5" />
    </div>
  );
};
