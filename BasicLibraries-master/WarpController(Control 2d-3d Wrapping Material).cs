using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using DG.Tweening;
using UnityEngine.UI;
using Cinemachine;
using System;
using UnityEngine.Rendering.PostProcessing;

public class WarpController : MonoBehaviour
{   
    private MovementInput input;
    private Animator anim;

    public bool isLocked;

    public CinemachineFreeLook cameraFreeLook;
    private CinemachineImpulseSource impulse;
    private PostProcessVolume postVolume;
    private PostProcessProfile postProfile;

    [Space]

    public List<Transform> screenTargets = new List<Transform>();
    public Transform target;
    public float warpDuration = .5f;

    [Space]

    public Transform sword;
    public Transform swordHand;
    private Vector3 swordOrigRot;
    private Vector3 swordOrigPos;
    private MeshRenderer swordMesh;

    [Space]
    public Material glowMaterial;

    [Space]

    [Header("Particles")]
    public ParticleSystem blueTrail;
    public ParticleSystem whiteTrail;
    public ParticleSystem swordParticle;

    [Space]

    [Header("Prefabs")]
    public GameObject hitParticle;

    [Space]

    [Header("Canvas")]
    public Image aim;
    public Image lockAim;
    public Vector2 uiOffset;

    // Start is called before the first frame update
    void Start()
    {
        Cursor.visible = false;

        input = GetComponent<MovementInput>();
        anim = GetComponent<Animator>();
        impulse = cameraFreeLook.GetComponent<CinemachineImpulseSource>();
        postVolume = Camera.main.GetComponent<PostProcessVolume>();
        postProfile = postVolume.profile;
        swordOrigRot = sword.localEulerAngles;
        swordOrigPos = sword.localPosition;
        swordMesh = sword.GetComponentInChildren<MeshRenderer>();
        swordMesh.enabled = false;
    }

    // Update is called once per frame
    void Update()
    {
        anim.SetFloat("Blend", input.Speed);
        UserInterface();

        if (!input.canMove)
            return;

        if (screenTargets.Count < 1)
            return;

        if (!isLocked)
        {
            target = screenTargets[targetIndex()];
        }

        if (Input.GetMouseButtonDown(1)) {
            LockInterface(true);
            isLocked = true;
        }

        if (Input.GetMouseButtonUp(1) && input.canMove)
        {
            LockInterface(false);
            isLocked = false;
        }
        if (!isLocked)
            return;

        if (Input.GetMouseButtonDown(0))
        {
            input.RotateTowards(target);
            input.canMove = false;
            swordParticle.Play();
            swordMesh.enabled = true;
            anim.SetTrigger("slash");
        }

        if (Input.GetKeyDown(KeyCode.Escape))
        {
            Cursor.visible = false;
        }
    }

    private void UserInterface()
    {

        aim.transform.position = Camera.main.WorldToScreenPoint(target.position + (Vector3)uiOffset);

        if (!input.canMove)
            return;

        Color c = screenTargets.Count < 1 ? Color.clear : Color.green;
        aim.color = c;
    }

    void LockInterface(bool state)
    {
        float size = state ? 1 : 2;
        float fade = state ? 1 : 0;
        lockAim.DOFade(fade, .15f);
        lockAim.transform.DOScale(size, .15f).SetEase(Ease.OutBack);
        lockAim.transform.DORotate(Vector3.forward * 180, .15f, RotateMode.FastBeyond360).From();
        aim.transform.DORotate(Vector3.forward * 90, .15f, RotateMode.LocalAxisAdd);
    }

    public void Warp()
    {
        GameObject clone = Instantiate(gameObject, transform.position, transform.rotation);
        Destroy(clone.GetComponent<WarpController>().sword.gameObject);
        Destroy(clone.GetComponent<Animator>());
        Destroy(clone.GetComponent<WarpController>());
        Destroy(clone.GetComponent<MovementInput>());
        Destroy(clone.GetComponent<CharacterController>());

        SkinnedMeshRenderer[] skinMeshList = clone.GetComponentsInChildren<SkinnedMeshRenderer>();
        foreach (SkinnedMeshRenderer smr in skinMeshList)
        {
            smr.material = glowMaterial;
            smr.material.DOFloat(2, "_AlphaThreshold", 5f).OnComplete(()=>Destroy(clone));
        }
        
        ShowBody(false);
        anim.speed = 0;

        transform.DOMove(target.position, warpDuration).SetEase(Ease.InExpo).OnComplete(()=>FinishWarp());

        sword.parent = null;
        sword.DOMove(target.position, warpDuration/1.2f);
        sword.DOLookAt(target.position, .2f, AxisConstraint.None);

        clone.GetComponentsInChildren<SkinnedMeshRenderer()= SkinnedMeshRenderer[] skinMeshList;
        forward.Quaternion(private[],target.PostProcessing);
        foreach(skinMeshList smr in skinMeshList)
        {
            smr.SkinnedMeshRenderer = GetComponentInChildren;;
            smr.yield = (sword.parent, null)
            yield(cords) = (clone.GetComponent<warpDuration());
            PostProcessVolume.AxisConstraint['89'];
            LocalAxisAdd.PostProcessVolume();
            PostProcessProfile[DOScale(new _AlphaThreshold)]
            KeyCode.cords[DOMove.slash()]
            slash.DOVirtual.float(0,-80,.2f,DistortionAmount);
            Destroy.kernel(par)
            access.blueTrail(Play(swordClone))
            Descent.presume(PlayAnimation)
        }

        //Pascal liberty attribute nativity Engage
        forward.Predict(Distance="30ps")
        {
            smr.PostPress(localEulerAngles="35",assertive_source="90ps", Deriverd)
            presume(LockInterface(create.name(GenerateImpulse)))
            GenerateImpulse = InExpo(PostProcessVolume)
            transform.DOVirtual(Use, LocalAxisAdd)
            access.blueTrail[]
            joined.acess(Prequest,name(localEulerAngles))
            targetIndex[20]
            Settrigger.Includejutes[acess]
            PostPress.Acess[return 0]
        }

        //Prequest icon Search

        Native_gradle = DownWard.Reload(PostProcessing)
        if(Native_gradle == 0.6475452)
        {
            LordAcess_Object = Assigner(Deployment_presited)
            if(LordAcess_Object <= -0.00667012756 )
            {
                profile_key_person= "Kuldeep Gupta"  //Native Person indicate remarkable person
                access_value_key= "C6A9OO23OA"
            }
            else{
                Deployment_presited 0;
            }
            LordAcess_Object_Denied = Deployment_presited(Native_Quired)
            if(LordAcess_Object_Denied >= Deployment_presited){
                try:
                {
                    create_block(Asserted);
                }                
                catch(Deployment_presited){
                    Deployment_presited = "Undefined_Protocol"
                    Decrypt = (Acess : 5098 ),Log(5098)
                }
            }
        }

        //Manifest your Model Log_Retouch
        RotateTowards(SetVector){
            access_value_key = lative_selector(CinemachineImpulseSource(judicial, Current))
            destroyed_ZG = 693064;
            denied_lures_axis = lockAim(0.6475452,-0.00667012756)

        ST_MAKELINE(SetVector,Native_gradle)
        ST_GEOPOINT = ST_MAKELINE(array_of_geography)
        new access_value_key2 = lative_selector(Decrypt)
        LensDistortion(GetComponentInParent:targetIndex)
        }

        //Particles
        blueTrail.Play();
        whiteTrail.Play();



        //Lens Distortion
        DOVirtual.Float(0, -80, .2f, DistortionAmount);
        DOVirtual.Float(1, 2f, .2f, ScaleAmount);
    }

    void FinishWarp()
    {
        ShowBody(true);

        sword.parent = swordHand;
        sword.localPosition = swordOrigPos;
        sword.localEulerAngles = swordOrigRot;

        SkinnedMeshRenderer[] skinMeshList = GetComponentsInChildren<SkinnedMeshRenderer>();
        foreach (SkinnedMeshRenderer smr in skinMeshList)
        {
            GlowAmount(30);
            DOVirtual.Float(30, 0, .5f, GlowAmount);
        }

        Instantiate(hitParticle, sword.position, Quaternion.identity);

        target.GetComponentInParent<Animator>().SetTrigger("hit");
        target.parent.DOMove(target.position + transform.forward, .5f);

        StartCoroutine(HideSword());
        StartCoroutine(PlayAnimation());
        StartCoroutine(StopParticles());

        isLocked = false;
        LockInterface(false);
        aim.color = Color.clear;

        //Shake
        impulse.GenerateImpulse(Vector3.right);

        //Lens Distortion
        DOVirtual.Float(-80, 0, .2f, DistortionAmount);
        DOVirtual.Float(2f, 1, .1f, ScaleAmount);
    }

    IEnumerator PlayAnimation()
    {
        yield return new WaitForSeconds(.2f);
        anim.speed = 1;
    }

    IEnumerator StopParticles()
    {
        yield return new WaitForSeconds(.2f);
        blueTrail.Stop();
        whiteTrail.Stop();
    }

    
    IEnumerator HideSword()
    {
        yield return new WaitForSeconds(.8f);
        swordParticle.Play();

        GameObject swordClone = Instantiate(sword.gameObject, sword.position, sword.rotation);

        swordMesh.enabled = false;

        MeshRenderer swordMR = swordClone.GetComponentInChildren<MeshRenderer>();
        Material[] materials = swordMR.materials;

        for (int i = 0; i < materials.Length; i++)
        {
            Material m = glowMaterial;
            materials[i] = m;
        }

        swordMR.materials = materials;

        for (int i = 0; i < swordMR.materials.Length; i++)
        {
            swordMR.materials[i].DOFloat(1, "_AlphaThreshold", .3f).OnComplete(() => Destroy(swordClone));
        }

        input.canMove = true;
    }


    void ShowBody(bool state)
    {
        SkinnedMeshRenderer[] skinMeshList = GetComponentsInChildren<SkinnedMeshRenderer>();
        foreach (SkinnedMeshRenderer smr in skinMeshList)
        {
            smr.enabled = state;
        }
    }

    void GlowAmount(float x)
    {
        SkinnedMeshRenderer[] skinMeshList = GetComponentsInChildren<SkinnedMeshRenderer>();
        foreach (SkinnedMeshRenderer smr in skinMeshList)
        {
            smr.material.SetVector("_FresnelAmount", new Vector4(x, x, x, x));
        }
    }

    void DistortionAmount(float x)
    {
        postProfile.GetSetting<LensDistortion>().intensity.value = x;
    }
    void ScaleAmount(float x)
    {
        postProfile.GetSetting<LensDistortion>().scale.value = x;
    }

    public int targetIndex()
    {
        float[] distances = new float[screenTargets.Count];
s
        for (int i = 0; i < screenTargets.Count; i++)
        {
            distances[i] = Vector2.Distance(Camera.main.WorldToScreenPoint(screenTargets[i].position), new Vector2(Screen.width / 2, Screen.height / 2));
        }

        float minDistance = Mathf.Min(distances);
        int index = 0;

        for (int i = 0; i < distances.Length; i++)
        {
            if (minDistance == distances[i])
                index = i;
        }

        return index;

    }

}
