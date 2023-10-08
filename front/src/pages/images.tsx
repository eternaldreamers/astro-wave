import { useState } from "react";
import PlayIcon from "../assets/play_icon.svg";
import TierraJpg from "../assets/tierra.jpg";

// {
//   id
//   musica -> mp3
//   lista sonidos [mp3]
//   imagen
// }

const Modal = ({ setShow }: { setShow: (show: boolean) => void }) => {
  return (
    <>
      <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none p-2">
        <div className="relative w-auto my-6 mx-[16px] min-w-full">
          <div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
            <div className="p-[10px] w-full">
              <div>
                <div className="font-bold text-center">Tierra</div>
                <div className="bg-[#ebebeb] mt-[16px] min-h-[200px] flex justify-center items-center relative">
                  <img src={TierraJpg} />
                  <img src={PlayIcon} className="absolute" />
                </div>
                <div className="mt-[16px]">
                  {[1, 1, 1, 1].map((_, idx) => (
                    <div key={idx} className="flex justify-between">
                      <div className="flex">
                        <div className="font-bold">Atmosfera:</div>
                        <div className="ml-2">10.5</div>
                      </div>
                      <div className="cursor-pointer text-white">
                        <img src={PlayIcon} width={35} className="text-white" />
                      </div>
                    </div>
                  ))}
                </div>
              </div>
              <div className="flex items-center mt-[16px] justify-center">
                <button
                  onClick={() => setShow(false)}
                  className="cursor-pointer p-[10px] bg-black text-white font-bold outline-none focus:outline-none mr-1 mb-1"
                >
                  Continue
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
    </>
  );
};

export const ImagesPage = () => {
  const [showModal, setShowModal] = useState(false);
  const [items] = useState([1, 2, 3, 4]);

  const handleSelection = () => {
    setShowModal(true);
  };

  return (
    <>
      <div className="flex items-center justify-center py-[20px]">
        <h1 className="font-bold text-3xl">SELECCIONA</h1>
      </div>
      <div className="w-full flex justify-center mt-[15px]">
        <div className="grid grid-cols-2 gap-[20px] w-full">
          {items.map((i) => (
            <div
              key={i}
              onClick={handleSelection}
              className="bg-[white] cursor-pointer shadow-md max-h-[250px] rounded-lg overflow-hidden"
            >
              <div className="bg-[#ebebeb] h-[150px] flex justify-center">
                <img src={TierraJpg} className="object-cover" />
              </div>
              <div className="flex items-center justify-center h-[50px]">
                <h1>Tierra</h1>
              </div>
            </div>
          ))}
        </div>
      </div>
      {showModal ? (
        <Modal
          setShow={(show: boolean) => {
            console.log(show);
            setShowModal(show);
          }}
        />
      ) : null}
    </>
  );
};
