import React, { useRef, useEffect } from "react";

const { tableau } = window;


function TableauEmbed () {
    const ref = useRef(null);
    const url = "https://public.tableau.com/views/Book2_16742399644750/Sheet2?:language=en-US&:display_count=n&:origin=viz_share_link";

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

export default TableauEmbed;