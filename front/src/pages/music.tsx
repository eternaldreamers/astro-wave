import service from "../services";
import { useEffect, useState } from "react";
import { FaPlay } from "react-icons/fa6";
// import { useEffect, useState } from "react";
import WaveSurfer from "wavesurfer.js";

export const MusicPage = () => {
  // const [isPlaying, setPlaying] = useState(false);
  // const [surface, setSurface] = useState(null)

  // useEffect(() => {
  //   const track = document.querySelector("#track");
  //   // Unable to decode audio data
  //   const waveSurface = WaveSurfer.create({
  //     container: "#waveform",
  //     waveColor: 'rgb(200, 0, 200)',
  //     progressColor: 'rgb(100, 0, 100)',
  //     url: 'https://www.mfiles.co.uk/mp3-downloads/gs-cd-track2.mp3',
  //   });
  //   waveSurface.load(track);

  //   setSurface(waveSurface)
  // }, []);

  // const handlePlay = () => {
  //   setPlaying(!isPlaying);
  //   surface.playPause();
  //   // trackRef.current
  // };

  const [resource, setResource] = useState(null);

  useEffect(() => {
    const data = service.getMusic();
    console.log(data);
  }, []);

  return (
    <>
      <div className="flex items-center justify-center py-[20px]">
        <h1 className="font-bold text-3xl">Listen carefully</h1>
      </div>
      <div className="w-full flex justify-center mt-[15px]">
        <div className="bg-[white] cursor-pointer shadow-md rounded-lg overflow-hidden w-full p-3">
          <div className="w-full flex items-center justify-between">
            <div>text</div>
            <div className="cursor-pointer">
              <FaPlay />
            </div>
          </div>
        </div>
      </div>
    </>

    // <div className="w-full h-screen flex justify-center items-center">
    //   <div>
    //     <div className="bg-[blue] min-w-[500px]">
    //       <div className="flex flex-row align-center justify-center h-[100px] w-full bg-transparent">
    //         <div
    //           onClick={handlePlay}
    //           className="flex justify-center w-[60px] h-[60px] bg-[#EFEFEF] rounded-[50%] border-none outline-none cursor-pointer pb-[3px]"
    //         >
    //           {!isPlaying ? "play" : "Pause"}
    //         </div>
    //         <div id="waveform" className="w-full h-[90px]" />
    //         sdf
    //         <audio id="track" />
    //       </div>
    //     </div>
    //   </div>
    // </div>
  );
};
