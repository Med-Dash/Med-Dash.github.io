import React, { useRef, useEffect } from "react";

const { tableau } = window;


function TableauEmbed() {
    const ref = useRef(null);
    const url = "https://public.tableau.com/views/LongitudinalDashboardPatient1/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link";

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
