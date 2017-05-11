//contres.h
#ifndef CONTRES_H
#define CONTRES_H

#ifdef __cplusplus
extern "C" {  // only need to export C interface if used by C++ source code
#endif

#include "common.h"

typedef unsigned int bool;

#ifdef __linux__

	void sfd2(double* H, double* dH, double r);

	void sfd6(double* H, double* dH, double r, double s);

        void getAABB(float64* AABBmin, float64* AABBmax, int nsd, int nnod, float64* X, float64 longestEdge, int32* IEN, int32* ISN, uint32* elementID, uint32* segmentID, int n, int nsn, int nes, int nen, int neq);

        void assembleContactResidualAndStiffness(float64* Gc, float64* vals, float64* rows, float64* cols, int* len, float64* GPs, int32* ISN, int32* IEN, float64* X, float64* U, float64* H, float64* dH, float64* gw, float64* activeGPsOld, int neq, int nsd, int npd, int ngp, int nes, int nsn, int nen, int GPs_len, float64 epss, bool keyContactDetection, bool keyAssembleKc);

	void getLongestEdgeAndGPs(float64* longestEdge, float64* GPs, int n, int nsd, int ngp, int neq, int nsn, int nes, int nen, uint32* elementID, uint32* segmentID, int32* ISN, int32* IEN, float64* H, float64* X);

	void evaluateContactConstraints(float64* GPs, int32* ISN, int32* IEN, int32* N, float64* AABBmin, float64* AABBmax, int* head, int* next, float64* X, uint32* elementID, uint32* segmentID, int n, int nsn, int nsd, int npd, int ngp, int nen, int nes, int neq, float64 longestEdge);
#elif _WIN32
			  // windows code goes here

	void __declspec(dllexport) sfd2(float64* H, float64* dH, float64 r);
	void __declspec(dllexport) sfd6(float64* H, float64* dH, float64 r, float64 s);
	void __declspec(dllexport) getAABB(float64* AABBmin, float64* AABBmax, int nsd, int nnod, float64* X, float64 longestEdge, int32* IEN, int32* ISN, uint32* elementID, uint32* segmentID, int n, int nsn, int nes, int nen, int neq);

	void __declspec(dllexport) assembleContactResidualAndStiffness(float64* Gc, float64* vals, float64* rows, float64* cols, int* len, float64* GPs, int32* ISN, int32* IEN, float64* X, float64* U, float64* H, float64* dH, float64* gw, float64* activeGPsOld, int neq, int nsd, int npd, int ngp, int nes, int nsn, int nen, int GPs_len, float64 epss, bool keyContactDetection, bool keyAssembleKc);

	void __declspec(dllexport) getLongestEdgeAndGPs(float64* longestEdge, float64* GPs, int n, int nsd, int ngp, int neq, int nsn, int nes, int nen, uint32* elementID, uint32* segmentID, int32* ISN, int32* IEN, float64* H, float64* X);

	void __declspec(dllexport) evaluateContactConstraints(float64* GPs, int32* ISN, int32* IEN, int32* N, float64* AABBmin, float64* AABBmax, int* head, int* next, float64* X, uint32* elementID, uint32* segmentID, int n, int nsn, int nsd, int npd, int ngp, int nen, int nes, int neq, float64 longestEdge);
#else

#endif

#ifdef __cplusplus
}
#endif

#endif  // CONTRES_H
