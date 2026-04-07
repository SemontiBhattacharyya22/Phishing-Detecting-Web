from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .utils import analyze_email, analyze_url
from .models import EmailScan
# from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def detect_email(request):
    email = request.data.get("email", "")
    result = analyze_email(email)

    EmailScan.objects.create(
        user=request.user,
        email_text=email,
        prediction=result["prediction"],
        confidence=result["confidence"],
        score=result["score"]
    )

    return Response(result)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_url(request):
    url = request.data.get("url", "")
    reasons = analyze_url(url)

    return Response({
        "url": url,
        "is_suspicious": bool(reasons),
        "reasons": reasons
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def history(request):
    scans = EmailScan.objects.filter(user=request.user)

    return Response([
        {
            "email": s.email_text[:50],
            "prediction": s.prediction,
            "confidence": s.confidence,
            "date": s.created_at
        } for s in scans
    ])


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def stats(request):
    total = EmailScan.objects.filter(user=request.user).count()
    phishing = EmailScan.objects.filter(user=request.user, prediction="Phishing").count()

    return Response({
        "total": total,
        "phishing": phishing,
        "safe": total - phishing
    })