using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TokenScript : MonoBehaviour
{
    public string curColor; 

    // Start is called before the first frame update
    void Start()
    {
        curColor = gameObject.tag;
        GetComponent<CircleCollider2D>().enabled = false;
        StartCoroutine(Delay());
    }

    // Update is called once per frame
    void Update()
    {
        if (gameObject.tag == "UL")
        {
            //
            if ((GameScript.ULStatus == "y") && (curColor == "black"))
            {
                GetComponent<SpriteRenderer>().color = new Color(1, 1, 1);
                gameObject.tag = "white";
            }

            if ((GameScript.ULStatus == "y") && (curColor == "white"))
            {
                GetComponent<SpriteRenderer>().color = new Color(0, 0, 0);
                gameObject.tag = "black";
            }

            //
            if ((GameScript.ULStatus == "r") && (curColor == "black"))
            {
                gameObject.tag = "black";
            }

            if ((GameScript.ULStatus == "r") && (curColor == "white"))
            {
                gameObject.tag = "white";
            }

        }
    }

    IEnumerator Delay()
    {
        yield return new WaitForSeconds(2);
        GetComponent<CircleCollider2D>().enabled = true;
    }
}
