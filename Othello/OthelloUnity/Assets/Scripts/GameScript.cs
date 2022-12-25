using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameScript : MonoBehaviour
{
    public Transform Tile;
    public static string currentTurn = "white";
    public static string ULStatus = "n";

    // Start is called before the first frame update
    void Start()
    {
        //making tile boards
        //Vertical Tile Loop
        for (float y = 4; y > -5; y -= 1.3f)
        {
            //Horizontal Tile loop
            for (float x = -4; x < 5; x += 1.3f)
            {
                Instantiate(Tile, new Vector2(x, y), Tile.rotation);
            }

        }

        Debug.Log("Board Created");
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
