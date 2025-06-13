from mcp.server.fastmcp import FastMCP
from gradio_client import Client
import sys
import io
import json 

mcp = FastMCP("utp")




@mcp.tool()
async def od_visualizer(csv_data : str =""",source,target,value
        0,0,0,9622
        1,0,1,26598
        2,0,2,6392
        3,0,3,1782
        4,0,4,1063
        5,0,5,647
        6,0,6,113
        7,0,7,2
        8,1,0,26539
        9,1,1,313129
        10,1,2,92552
        11,1,3,20102
        12,1,4,7240
        13,1,5,4175
        14,1,6,644
        15,1,7,13
        """) -> str:
    """A quick visualizer that displays trip flow numbers and shares using a directed chord diagram
    
    Args:
        param_0: CSV data containing source, target, and value columns
    """
    # from gradio_client import Client
    client = Client("http://trnscd17:7070/od2chord/")
    result = client.predict(
                param_0=csv_data,
                api_name="/predict"
        )
    return result[1]


if __name__ == "__main__":
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    mcp.run(transport='stdio')