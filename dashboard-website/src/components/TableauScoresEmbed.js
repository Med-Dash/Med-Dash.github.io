import React, { useRef, useEffect } from "react";

const { tableau } = window;


function TableauScoresEmbed() {
    const ref = useRef(null);
    const url = "https://public.tableau.com/shared/RMYZPXWW7?:display_count=n&:origin=viz_share_link";

    function initViz () {
        new tableau.Viz(ref.current, url);
    }
    useEffect(() => {
        initViz();
    }, [])
    return (
        <div>
            <div ref={ref}></div>
        </div>
    );
}



export default TableauScoresEmbed;