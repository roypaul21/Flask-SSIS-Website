using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ClickTileScript : MonoBehaviour
{
    public Transform WhiteToken;
    public Transform BlackToken;
    public Transform ULprobe;

    private void OnMouseDown()
    {

        if (GameScript.currentTurn == "white")
        {
            Instantiate(WhiteToken, transform.position, WhiteToken.rotation);
            Debug.Log("Token White");
            StartCoroutine(waitCurrentTurnB());
            //GameScript.currentTurn = "black";
            GetComponent<BoxCollider2D>().enabled = false;

            Instantiate(ULprobe, transform.position, ULprobe.rotation);
        }
        else
        if (GameScript.currentTurn == "black")
        {    
            Instantiate(BlackToken, transform.position, BlackToken.rotation);
            Debug.Log("Token Black");
            StartCoroutine(waitCurrentTurnW());
            //GameScript.currentTurn = "white";
            GetComponent<BoxCollider2D>().enabled = false;

            Instantiate(ULprobe, transform.position, ULprobe.rotation);
        }

    }

    IEnumerator waitCurrentTurnW()
    {
        yield return new WaitForSeconds(6);
        GameScript.currentTurn = "white";
        GameScript.ULStatus = "n";
    }

    IEnumerator waitCurrentTurnB()
    {
        yield return new WaitForSeconds(6);
        GameScript.currentTurn = "black";
        GameScript.ULStatus = "n";
    }
}
